


from operator import truediv
from AppBaseTask import RepeatingTask, ETaskResult, TaskParent

from AppDefs import DirDefs

from FileSystem import AsyncFileTaskMgr, FileSystemOps, FileOpParent, EFileDataType

from AppUtils import RequestUrl, FileOperation, Logger



#
# All Stocks Task - we'll use a git repository to pull all stocks/company names from
#
class AllStocksTask( RepeatingTask, FileOpParent ):

    ALL_STOCKS_DIR      = DirDefs.addToCacheDir( "ALL_STOCKS" )
    US_SYMBOLS_DIR      = DirDefs.makePath( ALL_STOCKS_DIR, "US_STOCKS" )
    
    US_GIT_CLONE_CMD    = "git clone https://github.com/rreichel3/US-Stock-Symbols.git"
    US_GIT_UPDATE_CMD   = "git --git-dir=" + US_SYMBOLS_DIR + " fetch origin"
    
    COMPANY_INFO_FILE   = DirDefs.makePath( ALL_STOCKS_DIR, "CompanyInfo_{}.txt" )   # one per month

    US_EXCHANGES        = [ "amex", "nyse", "nasdaq" ]


    # init ourself
    def __init__( self, parent: TaskParent ):
        
        RepeatingTask.__init__( self, "AllStocksTask", parent )
        
        FileSystemOps.createDir( self.ALL_STOCKS_DIR )
        FileSystemOps.createDir( self.US_SYMBOLS_DIR )
   
        self.sleepTimeout   = int(2)
        self.requestFiles   = True
        self.startReadOps   = True
        self.procFilesCnt   = int(0)

        self.files: list[str] = []
        for exchange in self.US_EXCHANGES:
            self.files.append( DirDefs.makePath( self.US_SYMBOLS_DIR, (exchange + ".json") ) ) # type: ignore

        self.fileOps = [ FileOperation.createReadFileOp( self.files[0], self, False ) ]
        self.fileOps.append( FileOperation.createReadFileOp( self.files[1], self, False ) )
        self.fileOps.append( FileOperation.createReadFileOp( self.files[2], self, False ) )
        
        for fileOp in self.fileOps: # type: ignore
            fileOp.data.type = EFileDataType.eString

        self.__startTask__()


    # make the url request
    def __makeRequest__(self):

        rsp = None
        if not FileSystemOps.doesDirExist( self.US_SYMBOLS_DIR ):
            rsp = RequestUrl.get( self.US_GIT_CLONE_CMD )
        else:
            rsp = RequestUrl.get( self.US_GIT_UPDATE_CMD )

        if rsp:
            return True
        return False


    # file operation callback
    def fileOpComplete( self, fileOp: FileOperation ):

        if not fileOp.result.result:

            # if failed rerequest the read if its the first error only
            if fileOp.result.failCnt == 0:
                
                if len( fileOp.result.error ) > 0:
                    Logger.err( f"AllStocksTask Read File Error: {fileOp.result.error}" )
                
                fileOp.result.reset()
                fileOp.result.failCnt += 1
                AsyncFileTaskMgr.requestFileOp( fileOp )
                
                

    # process the files we just retrieved from github - request to read our files
    def requestToReadFiles( self ):
        
        for fileOp in self.fileOps: # type: ignore
            AsyncFileTaskMgr.requestFileOp( fileOp )

        self.requestFiles = False
            
 
    # our processing task thread function
    def processTask(self) -> ETaskResult:

        if self.requestFiles:

            if not self.__makeRequest__():
                 return ETaskResult.eSucceeded

        else:

            #  start the read file operations
            if self.startReadOps:
                self.requestToReadFiles()
                self.startReadOps = False
            else:
                self.processReadFiles()

                if self.checkForUnfinishedReads():
                    return ETaskResult.eSucceeded
          
        return ETaskResult.eSucceeded


    # see if we are finished
    def isFinished( self ) -> bool:

        for fileOp in self.fileOps: # type: ignore           
            if not fileOp.result.done:
                return False
        return True


    # check for unfinished reads
    def checkForUnfinishedReads( self ):
    
        if self.isFinished():
            self.repeat = False
            return True

        # 8 minutes all reads should be done if not log error
        if self.procFilesCnt > 4: 

            for fileOp in self.fileOps: # type: ignore
                if not fileOp.result.done:
                    Logger.err( f"Unable to read AllStocksTask File: {fileOp.filepath}. Exiting the Task..." )
            return True         

        return False


    # process file data and make sure we got all the data
    def processReadFiles( self ):

        self.procFilesCnt += 1

        for fileOp in self.fileOps: # type: ignore
            
            if fileOp.result.done:
                
                companyDefinitions = fileOp.data.blob.split( "}," )

                for companyDef in companyDefinitions:

                    # todo:
                    #companyInfo             = DailyCompanyInfo()
                    #companyInfo.exchange    = self.US_EXCHANGES[ exchange ] 
                    #companyInfo.parseJsonText( companyDef.split( "," ) )

                    #companies[ companyInfo.getName() ] = companyInfo

                #exchange += 1

            #theApp.setAllCompanyStocks( companies )
            
            #Log.info( "GetAllStocks -> theApp.setCompanies: {}".format( self._companiesByName.keys().count() ) )
'''