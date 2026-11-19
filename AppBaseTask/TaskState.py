
from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod

from AppBaseTask import Task


#
# Task State Enum
#
class ETaskState( Enum ):

    eUnknown            = int(0)    # invalid state
    eInitial            = int(1)    # initialized and registered
    eStarting           = int(2)    # task is starting to run
    eRunning            = int(3)    # task is running
    eSleeping           = int(4)    # task is waiting to run again
    eDone               = int(5)    # task is done..forever [single shot task]
    eDoneForced         = int(6)    # done w/ forced exit
    eDoneFailed         = int(7)    # ran but failed and is done...forever [single shot task]
    eDoneExcepted       = int(8)    # ran but excepted and is done...forever [single shot task]
    eMax                = int(9)    # used for loops



#
# the State of the Task
#
class StateOfTask:

    def __init__( self ):

        self.stateTransTime = [ datetime.fromtimestamp( 0 ) ] * ETaskState.eMax.value   # a datetime for each ETaskState
        self.state          = ETaskState.eUnknown
        self.prevState      = ETaskState.eUnknown
        self.nextState      = ETaskState.eUnknown
            
    
    # set the new state..everyone should go through here
    def setState(self, state: ETaskState ):

        self.prevState    = self.state
        self.state        = state
        self.nextState    = int( state.value + 1 )
# todo:        self.stateTransTime[ int(state.value) ] = DTUtils.getCurTime()
        
    # get a task state as a string
    @staticmethod
    def statetoString( state: int ) -> str:

        states = [ "Unknown", "Initialized", "Starting", "Running", "Sleeping", "Finished", "Finished Forced", "Finished Failed", "Max State" ]
        if state >= ETaskState.eUnknown.value and state < ETaskState.eMax.value:
            return states[ state ]
        return "Unknown"


#
# Abstract Task Parent
# 
class AbstractTaskParent(ABC):

    @abstractmethod
    def taskComplete(self, task: Task ) -> None:
        pass


#
# All task creators must derive from Task Parent for the callback
#
class TaskParent( AbstractTaskParent ):

    def __init__( self, name: str ):
        self.name = name

    # function must be implemented by derived class
    def taskComplete( self, task: Task ) -> None:
        assert( False ) 
        # todo: check for errors and clean up



#
# Task State - holds the process state of the task
# 
# all users of tasks must have a taskComplete callback function
#       
class TaskState():

    __TaskID__ = int(776)         # next task id, hidden from others

    # get an always unique runtime task id
    @staticmethod
    def __getUniqueUID__() -> int:
    
        TaskState.__TaskID__ += 1
        return TaskState.__TaskID__

    
    # init ourself
    def __init__( self, taskName: str, repeatTask: bool, parent: TaskParent ):

        self.taskId         = self.__getUniqueUID__()
        self.taskName       = taskName
        self.repeat         = repeatTask
        self.parent         = parent
        self.error          = ""     
        self.errorCnt       = int(0)
        self.sleepTimeout   = int(5)    # default to 5 minutes sleep between run()s, only used when a we are a repeating task
        self.stateOfTask    = StateOfTask()
              
        self.stateOfTask.setState( ETaskState.eInitial )
    
      
    def __clearTransitionTimes__( self, state: ETaskState ):
        
        index = int(state.value)

        while index < int( ETaskState.eMax.value ):
            self.stateOfTask.stateTransTime[ index ] = datetime.fromtimestamp( 0 )  
            index += 1

