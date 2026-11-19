


'''



from enum import Enum
import datetime
from xmlrpc.client import DateTime

from App import theApp
from AppTasks import EarningsCalendarTask
from AppTasks.BaseTask import ETaskResult
from AppTasks.TaskUtils import RepeatingTask, FunctionPtrTask
from AppUtils import Log, DateTimeFormat, GuardedList, DTUtils


#
# App Task - perform background tasks for the application level
#
class AppTask( RepeatingTask ):

    class EWorkTasks( Enum ):
        eCompressDirs        = int(0)
        #eDeleteFiles        = int(1)
        eDecompressDirs      = int(1)



    # init
    def __init__( self ):

        RepeatingTask( "AppTask", theApp )
        
        self._curWorkTask    = self.EWorkTasks.eCompressDirs
        self._oneDayAhead    = None
        self._dirsToCompress = GuardedList()
        
        self._sleepTimeout   = int(3)
        
        self._startTask__()


    # run once a day tasks
    def runOnceADayTasks( self ):

        EarningsCalendarTask( self )



    # compress a directory for a task at a certain time
    def compressDirectory( self, dirName: str, compressAfterTime: datetime ):
        self._dirsToCompress.addItem( (compressAfterTime, dirName) )


    # todo: put try ...exept in all process task functions


    # our processing task thread function
    def processTask(self) -> bool:
    
        try:

            # if not init run once a day tasks
            if self._oneDayAhead == None:
                self.__runOnceADayTasks__()
                self._oneDayAhead   = (DTUtils.getCurTime() + DTUtils.getHoursTimeDelta( int(24) ))

            # if a day has passed run once a day tasks
            if DTUtils.getCurTime() > self._oneDayAhead:
                self.__runOnceADayTasks__()
                self._oneDayAhead   = (DTUtils.getCurTime() + DTUtils.getHoursTimeDelta( int(24) ))


            # perform a different EWorkTask every time we come through here
            match self._curWorkTask:

                case self.EWorkTasks.eCompressDirs:
                    self.__checkCompressDirectoryTimes__()


        except:
            Log.error( "AppTask.processTask - Exception while processing work task: {}".format( self._curWorkTask ) )
            return False

        return True


    # check future directories to compress to see if the compress time has arrived
    def __checkCompressDirectoryTimes__( self ):

        index = int(0)
        while index < self._dirsToCompress.getCount():
           
            compressTimePathPair = self._dirsToCompress.getItem( index )
          
            compressAfterTime    = compressTimePathPair[0]
            if datetime.now() > compressAfterTime:
                
                dirToCompress    = compressTimePathPair[1]
                Log.info( "Compressing directory: {} at {}".format( dirToCompress, DateTimeFormat.getDateTime() ) )
                
                # todo: compress the directory

                self._dirsToCompress.popItem( index )
                index -= 1

            index += 1





    # decompress a directory for a historical search task



    # watch files for the application



    # check active gui is working fine


    # todo: add robinhood api

    # schedule other tasks


    # todo: other tasks


    # one of our task's is done
    def taskComplete( self, task ):
        
        del task
        task = None

   
   
   '''