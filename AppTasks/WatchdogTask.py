
'''

from datetime import timedelta, datetime

#from App import theApp

#from AppUtils import GuardedList, DTUtils

from AppBaseTask import Task, ETaskResult

from AppTasks import TaskManager



#
# the Watchdog Task
#
class WatchdogTask( Task ):
    

    # init
    def __init__(self):
 
        Task.__init__( self, "WatchdogTask", True, theApp.getTaskMgr() )
    
        self._problemTasks  = GuardedList()             
        
        self._allTasks      = []
        self._allTasks.copy( theApp.getTaskMgr().getAllTasks() )

        self._sleepTime     = int(5)
        self._timer.start( self._sleepTime )
           



    # get field names for our view
    #def getFieldNames(self) -> list[str]:
    #    return self.FIELD_NAMES 


    # restart task if they are done running
    def __restartTasks__( self ):
        
        runningTasks    = []
        restartTasks    = []
        
        # copy tasks to restart onto temp list
        restartTasks.copy( self._tasksToRestart )
        
        # start the tasks is they are done running
        for task in restartTasks:
                   
            if task.state != EBaseTaskState.eRunning and task.state != EBaseTaskState.eStarting:
                theApp.getTaskMgr().startTask( task )
            else:
                runningTasks.append( task )
        
        # put running tasks back on tasks to restart list for later
        if len( self._tasksToRestart ) > 0:
            runningTasks.extend( self._tasksToRestart )
                
        self._tasksToRestart.clear()
        self._tasksToRestart.copy( runningTasks )
        
    
    # handle the unknown state - the task should never be in unknown for more than a second
    def __handleUnknownState__( self, task ):
        
        task.watchdogInfo.errorCnt += 1
        task.watchdogInfo.nextState = EBaseTaskState.eInitialized
    
    
    # the task has been initialized
    def __handleInitState__( self, task ):
        
        if task.watchdogInfo.nextState == EBaseTaskState.eInitialized:
            self.__checkNextStateTime__( task )
        else:
            self.__logBaseTaskStateError__( task )
        
        task.watchdogInfo.nextState = EBaseTaskState.eStarting
        self.__computeNextStateTime__( task )
    

    # the task is starting to run
    def __handleStartingState__( self, task ):

        if task.watchdogInfo.nextState == EBaseTaskState.eStarting:
            self.__checkNextStateTime__( task )
        else:
            self.__logBaseTaskStateError__( task )

        task.watchdogInfo.nextState = EBaseTaskState.eRunning
        self.__computeNextStateTime__( task )
        
        
    # the task is currently running
    def __handleRunningState__( self, task ):
    
        if task.watchdogInfo.nextState == EBaseTaskState.eRunning:
            self.__checkNextStateTime__( task )
        else:
            self.__logBaseTaskStateError__( task )

        task.watchdogInfo.nextState = EBaseTaskState.eWaiting
        self.__computeNextStateTime__( task )
        
    
    # the task is waiting to run set time it should run again
    def __handleWaitingState__( self, task ):

        if task.watchdogInfo.nextState == EBaseTaskState.eWaiting:
            self.__checkNextStateTime__( task )
        else:
            self.__logBaseTaskStateError__( task )

        task.watchdogInfo.nextState = EBaseTaskState.eRunning
        self.__computeNextStateTime__( task )

        
    # the task is complete and will never run again so clean it up
    def __handleCompleteState__( self, task ):

        if task.watchdogInfo.nextState == EBaseTaskState.eRunning:
            self.__checkNextStateTime__( task )
        else:
            self.__logBaseTaskStateError__( task )
            
        task.cleanup()
        

    # the task failed to run...see log file for error
    def __handleRunFailureState__( self, task ):

        task.state                  = EBaseTaskState.eFailComplete
        task.watchdogInfo.nextState = EBaseTaskState.eFailComplete
        task.cleanup()


    # the task failed but is complete
    def __handleFailCompleteState__( self, task ):
        
        task.cleanup()

        


    # process the tasks current state. make sure its not stalled and is still cycling...
    def __processBaseTaskState__( self, task: Task ):
                
        #taskLeavingCurStateTime   = task.__getTimeForNextState__()
        
        match task.state:
                    
            case ETaskState.eUnknown:
                self.__handleUnknownState__( task )

            case ETaskState.eInitialized:
                self.__handleInitState__( task )

            case ETaskState.eStarting:
                self.__handleStartingState__( task )

            case ETaskState.eRunning:
                self.__handleRunningState__( task )

            case ETaskState.eWaiting:    
                self.__handleWaitingState__( task )

            case ETaskState.eComplete:
                self.__handleCompleteState__( task )

            case ETaskState.eFailToRun:
                self.__handleRunFailureState__( task )

            case ETaskState.eFailComplete:
                self.__handleFailCompleteState__( task )
                                    
        # check for errors    
        if int(task.watchDogErrCnt) > 3:
            theApp.getTaskMgr().terminateTask( task )
        elif int(task.watchDogErrCnt) > 1:
            self.parent.taskRuntimeError( task )
            
            


    # we are here until told to exit 
    def processTask( self ) -> bool:

        try:

            self._allTasks.clear()
  
            self._allTasks.copy( theApp.getTaskMgr().getAllTasks() )

        
            # restart any task that need to be
            if self._tasksToRestart.count() > 0:
                self.__restartTasks__()


            # check all tasks are in a valid state and functioning


            # if we haven't requested all stocks do it now
            if self._reqAllStocksTime == Epocher.getTime():

                self._reqAllStocks.runRequestingTask()
                self._reqAllStocksTime = datetime.now()


            # request all stocks every 6 hours
            if self._reqAllStocksTime < (datetime.now() - timedelta( 0, 0, 0, 0, 0, 6, 0 )): 

                self._reqAllStocks.runRequestingTask()
                self._reqAllStocksTime = datetime.now()
        

            # check all tasks to make sure they are still alive and in the proper state. also clean up any complte tasks
        
            allActiveTasks   = theApp.getTaskMgr().getAllTasks()
            self._numEntries = len( allActiveTasks )
        
            taskNames        = allActiveTasks.keys()
            for taskName in taskNames:
        
                taskIdKeys   = allActiveTasks[ taskName ].keys()          
                for taskId in taskIdKeys:
               
                    task     = allActiveTasks[ taskName ][ taskId ]
                
                    if task != None:
                
                        # process the task
                        self.__processBaseTaskState__( task )
                    
                        # remove any completed tasks
                        if task.state >= TaskBase.EBaseTaskState.eComplete and task.state <= TaskBase.EBaseTaskState.eFailComplete:
                            theApp.getTaskMgr().deleteTask( task )
                 
                    else:
                    
                        # log error since the tqask should be valid
                        task        = Task( taskName )
                        task.id     = taskId
                        self.getClient().display( "WatchdogTask processTask Error: Task = {} - {} is invalid when the Task should still be valid".format( taskName, taskId ) )
                        theApp.getTaskMgr().deleteTask( task )

        except:



    # list to restart tasks once they are done running
    def restartTaskWhenDone( self, task ):
        
        self._tasksToRestart.append( task )
        
    
        '''