


from AppBaseTask import RepeatingTask, ETaskResult, TaskParent

from AppUtils import Logger

from typing import Callable, Any

#
# Repeating Function Pointer Task - a single shot task that calls a function somewhere
# 
class RepeatFuncPtrTask( RepeatingTask ):


    # init ourself
    def __init__( self, taskName: str, parent: TaskParent, sleepTime: int, func: Callable[ [list[Any]], None ], funcArgs: list[Any] = None ): # type: ignore

        RepeatingTask.__init__( self, taskName, parent )

        self.function    = func
        self.funcArgs    = funcArgs
        
        self.sleepTimeout  = int( sleepTime )

        self.__startTask__()


    # call the function to process our task
    def processTask(self) -> ETaskResult:
        
        try:

            self.function( self.funcArgs )
        
        except:

            Logger.err( f"FuncPtrTask.processTask for - {self.taskName} - threw an exception inside the function" )
            return ETaskResult.eExcepted

        return ETaskResult.eSucceeded


