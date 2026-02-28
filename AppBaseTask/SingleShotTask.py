

from AppBaseTask import Task, ETaskResult, TaskParent


#
# Single Shot Task - a task that just runs once
# 
class SingleShotTask( Task ):

    # init ourself
    def __init__( self, taskName: str, parent: TaskParent ):

        Task.__init__( self, taskName, False, parent )


    # the derived class must override this function
    def processTask(self) -> ETaskResult:
        
        self.error = "SingleShotTask processTask() must be overwritten by derived class"
        return ETaskResult.eFailed
        

