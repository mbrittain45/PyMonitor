
# pylint: disable=no-name-in-module
from PySide6.QtCore import QRunnable
from PySide6.QtCore import QObject, Slot, QTimer

from abc import ABC, abstractmethod
from enum import Enum

from AppBaseTask import TaskState, TaskParent, ETaskState
from AppUtils import Logger, DTUtils

from App.main import theStockApp

from typing import Any


# Task Result enum
class ETaskResult( Enum ):

    eUnknown        = int(0)
    eSucceeded      = int(1)
    eFailed         = int(2)
    eNumErrors      = int(3)
    eExcepted       = int(4)
    eForcedExit     = int(5)
  



#
# Task - base class for all tasks
#
# all users of tasks must overide:   
#
#   all Tasks must have this function since that is where their work is done
#   @abstractmethod
#   def processTask(self) -> bool:
#       pass
#
class Task( QRunnable, TaskState, QObject, ABC ):
        
    TASK_VIEW_FIELD_NAMES = [ "UID", "Name", "State", "Previous State", "Next State", "Next Runtime", "Last Error" ]

    # must be overridden
    @abstractmethod
    def processTask(self) -> bool:
        pass


    #    
    # init ourself
    #
    def __init__( self, taskName: str, repeatTask: bool, parent: TaskParent ):

        QRunnable.__init__(self)
        self.setAutoDelete( False )

        TaskState.__init__(self, taskName, repeatTask, parent )

        self.sleepTimeout   = int(5)
        self.result         = False
        self.exitFlag       = False
        self.nextRuntime    = 0
        self.cycleCount     = 0
 

    # get task status page data
    def getStatusData( self ) -> list[Any]:
        return [ self.taskId, self.taskName, self.stateOfTask.state, self.stateOfTask.prevState, self.stateOfTask.nextState, self.nextRuntime, self.error ]

 
    # our timer callback function
    @Slot()
    def wakeupTimerCallback(self):
        self.__startTask__()

       
    def exitTask( self ):
        self.exitFlag = True


    def __clearRuntimeData__(self):

        self.error          = ""
        #self.nextRuntime    = Epocher.getTime()
        #self.lastRuntime    = DTUtils.getCurTime()
        self.__clearTransitionTimes__( ETaskState.eRunning )


    # see if we were told to exit while we were sleeping
    def __shouldExitTask__( self ):

        if self.exitFlag:

            self.stateOfTask.setState( ETaskState.eDoneForced )
            self.__processComplete__()
            return True 

        return False



    def __processRepeatingTask__( self ):

        # if the task run failed 
        if not self.result:

            # if too many errors stop the task from repeating
            self.errorCnt += 1
            if self.errorCnt > 1:

                # set we are complete due too failures
                self.stateOfTask.setState( ETaskState.eDoneFailed )
                self.__processComplete__()
                theStockApp.getTaskMgr().updateTaskStatusPage( self )
                return 

        # if succeeded clear error count
        if self.result:
            self.errorCnt = 0
        
        # set state to sleeping awaiting wakeup timer
        self.stateOfTask.setState( ETaskState.eSleeping )

        timeout = int(self.sleepTimeout * int(1000)) # sleep for a few seconds

        # set our next runtime / wakeup time
        self.nextRuntime = (DTUtils.getCurTime() + DTUtils.getMsecTimeDelta( timeout ))
        
        # set our callback timer
        QTimer.singleShot( timeout, self, self.wakeupTimerCallback )

        theStockApp.getTaskMgr().updateTaskStatusPage( self )



    #
    # QRunnable calls run - this function and we call processTask() which all tasks must override
    #
    def run( self ):
        
        if self.repeat:
            theStockApp.getTaskMgr().updateTaskStatusPage( self )

        self.__clearRuntimeData__()

        if self.__shouldExitTask__():
            return

        self.stateOfTask.setState( ETaskState.eRunning ) # set our new running state

        if self.repeat:
            theStockApp.getTaskMgr().updateTaskStatusPage( self )        
        
        try:

            # call the derived task processTask() to do the actual work
            self._result = self.processTask()

            # wrap up the task processing this run
            if self.repeat:
                self.__processRepeatingTask__()
            else:
                self.__processComplete__()
                            
        except:

            #Log.error( "Task: {} with TaskId: {} and Object Id: {} excepted while running. Setting to Task Complete due to error".format( self.getName(), self.getUID(), id( self ) ) ) 
            #self.__setState__( self.EState.eFinishedExcepted )
            self.__processComplete__()


   
    # start ourself by calling the thread manager
    def __startTask__(self):
 
        self.stateOfTask.setState( ETaskState.eStarting )
# todo:
        # theApp.getTaskMgr().startTask( self )




    # process the result of run() -> processTask()
    def __processComplete__( self ):
        
        if self.stateOfTask.state == ETaskState.eDone:
            self.errorCnt = 0

        elif self.stateOfTask.state == ETaskState.eDoneForced:
            self.error = f"{self.taskName} - Task was forced to Exit by parent"

        elif self.stateOfTask.state == ETaskState.eDoneFailed:
            self.error = f"{self.taskName} - Task was forced to Completed state due to errors. It must be restarted by its parent"
       
        # set task to complete - done forever and ready to be deleted
    
        if len( self.error ) > 0:
            Logger.err( self.error )

        # tell our parent we are done completely
        if self.parent:                             # type: ignore
            self.parent.taskComplete( self )        # type: ignore
        
         
