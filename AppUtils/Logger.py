

from enum import Enum

from AppUtils import GuardedList, DateTimeFmt

from AppBaseTask import Task, TaskParent

from FileSystem import FileOperation, FileOpParent, AsyncFileTaskMgr

#
# Logger Msg Type
#
class ELogMsgType(Enum):

    eDEBUG = 1
    eINFO  = 2
    eWARN  = 3
    eERROR = 4
    eFATAL = 5


#
# Logger class - we are our own task parent
#
class Logger( Task, TaskParent, FileOpParent ):

    # make everything static
    enableTypes   = [ None, True, True, True, True ]               
    msgTypes      = [ "None", "DEBUG", "INFO", "WARNING", "ERROR", "FATAL" ]
    logmsgs       = GuardedList()   
    transactions  = GuardedList()   
    
    # init        
    def __init__( self ):

        Task.__init__( self, "LoggerTask", True, self )
        self.sleepTimeout = int(5)
            
        self.__startTask__()


    # process our task by logging to a file
    def processTask(self) -> bool:  # type: ignore

        if self.logmsgs.getCount() :
            
            logFile = f"./LogFiles/LogFile_{DateTimeFmt.getDate()}.txt"
            
            fileOp  = FileOperation.createWriteFileOp( logFile, self.logmsgs.getList(), self, False )
            
            if not AsyncFileTaskMgr.requestFileOp( fileOp ):
                assert( False )


        return True
    

    # tells when our task is done
    def taskComplete(self, task: Task ):
        assert( False ) # should never get here since we are a repeating task
    
    
    # queue the msg for logging via the ErrorLogTask
    @staticmethod
    def log( msg: str, msgType: ELogMsgType ):
        
        if Logger.enableTypes[ msgType.value ]:

            newMsg = "@ "
            newMsg += DateTimeFmt.getDateTime()
            newMsg += " MsgType: "
            newMsg += Logger.msgTypes[ msgType.value ]
            newMsg += " - Msg: "
            newMsg += msg
            newMsg += " \n"

            Logger.logmsgs.addItem( newMsg )
            
            # todo: status bar sent too
            #theApp.getStatuBar().displayMsg( newMsg )
            

    # log a warning msg
    @staticmethod
    def err( msg: str ):
        Logger.log( msg, ELogMsgType.eERROR )

    
    # log a warning msg
    @staticmethod
    def ewarn( msg: str ):
        Logger.log( msg, ELogMsgType.eWARN )

    
    # log an info msg
    @staticmethod
    def einfo( msg: str ):
        Logger.log( msg, ELogMsgType.eINFO )
        
    
    # log debug msg
    @staticmethod
    def edebug( msg: str ):
        Logger.log( msg, ELogMsgType.eDEBUG )

    
    # log debug msg
    @staticmethod
    def efatal( msg: str ):
        Logger.log( msg, ELogMsgType.eFATAL )

    
    # enable/disable certain msg types
    @staticmethod
    def enableMsgType( logType: ELogMsgType, enable: bool ):
        Logger.enableTypes[ logType.value ] = enable



