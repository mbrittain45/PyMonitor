
# pylint: disable=no-name-in-module
from PySide6.QtCore import QRunnable


from PySide6.QtCore import QObject, Slot #todo: QTimer, Slot

from abc import ABC, abstractmethod

#from datetime import datetime

from enum import Enum

from AppBaseTask import TaskState, TaskParent, ETaskState


''' TODO:
from PySide6.QtCore import QObject, Signal

class MyObject(QObject):
    my_signal = Signal() # pylint: disable=no-member
'''

#
# Task Result enum
#
class ETaskResult( Enum ):

    eUnknown        = int(0)
    eSucceeded      = int(1)
    eFailed         = int(2)
    eNumErrors      = int(3)
    eExcepted       = int(4)
    eForcedExit     = int(5)
  

#
# Abstract Task - all tasks must override processTask, which is where they do their work
#
class AbstractTask(ABC):

    @abstractmethod
    def processTask(self) -> ETaskResult:
        pass



#
# Task - base class for all tasks
#
# all users of tasks must overide:   
#
#   all Tasks must have this function since that is where their work is done
#   @abstractmethod
#   def processTask(self) -> ETaskResult:
#       pass
#
class Task( QRunnable, AbstractTask, TaskState, QObject ):
        
    TASK_VIEW_FIELD_NAMES = [ "UID", "Name", "State", "Previous State", "Next State", "Next Runtime", "Result", "Error" ]

    #    
    # init ourself
    #
    def __init__( self, taskName: str, repeatTask: bool, parent: TaskParent ):

        QRunnable.__init__(self)
        self.setAutoDelete( False )

        TaskState.__init__(self, taskName, repeatTask, parent )

        self.sleepTimeout   = int(5)
        self.result         = ETaskResult.eUnknown
        self.exitFlag       = False
#       self.lastRuntime    = DateTimeUtils.getCurTime() 
#       self.nextRuntime    = Epocher.getTime()
       
 
    # our timer callback function
    @Slot()
    def wakeupTimerCallback(self):
        self.__startTask__()

       
    def exitTask( self ):
        self.exitFlag = True


    def __clearRuntimeData__(self):

        self.error          = ""
        #self.nextRuntime    = Epocher.getTime()
        #self.lastRuntime    = DateTimeUtils.getCurTime()
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
        if self.result == ETaskResult.eFailed:
            # if too many errors stop the task from repeating
            self.errorCnt += 1
            if self.errorCnt > 1:
                # set we are complete due too failures
                self.stateOfTask.setState( ETaskState.eDoneFailed )
                self.__processComplete__()
                return 

        # if succeeded clear error count
        if self.result == ETaskResult.eSucceeded:
            self.errorCnt = 0
        
        # set state to sleeping awaiting wakeup timer
        self.stateOfTask.setState( ETaskState.eSleeping )
        #timeout = ( int(self.sleepTimeout) * int(60) ) * int(1000)
        # set our next runtime / wakeup time
        # TODO: self.nextRuntime = (DateTimeUtils.getCurTime() + DateTimeUtils.getMsecTimeDelta( timeout ))
        # set our callback timer
        #   QTimer.singleShot( timeout, self, self.wakeupTimerCallback )



    #
    # QRunnable calls run - this function and we call processTask() which all tasks must override
    #
    def run( self ):
        
        self.__clearRuntimeData__()

        if self.__shouldExitTask__():
            return

        self.stateOfTask.setState( ETaskState.eRunning ) # set our new running state
        
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
    
        # unregister ourself w/ the taskmgr
        #if self.stateOfTask.registered:
            # todo: theApp.getTaskMgr().unregisterTask( self )
        
        #if len( self.error ) > 0:
        # todo: Logger.error( self.error )

        # todo:
        # tell our parent we are done completely
        #self.parent.taskComplete( self )
        
         
