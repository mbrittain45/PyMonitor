

from AppBaseTask import SingleShotTask, TaskParent

from AppUtils import Logger

from typing import Callable

#
# Function Pointer Task - a single shot task that calls a function somewhere
# 
class FuncPtrTask( SingleShotTask ):


    # init ourself
    def __init__( self, taskName: str, parent: TaskParent, func: Callable[ [], None ], funcArgs: [] ): # type: ignore

        SingleShotTask.__init__( self, taskName, parent )

        self.function    = func         # type: ignore
        self.funcArgs    = funcArgs     # type: ignore
        
        self.__startTask__()


    # call the function to process our task
    def processTask(self) -> bool:
        
        try:

            self.function( self.funcArgs )      # type: ignore
        
        except:

            Logger.err( f"FuncPtrTask.processTask for - {self.taskName} - threw an exception inside the function" )
            return False

        return True


