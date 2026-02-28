


from AppBaseTask import Task, ETaskResult, TaskParent


#
# Repeating Task - a task that just runs repeatedly
# 
class RepeatingTask( Task ):

    # init ourself
    def __init__( self, taskName: str, parent: TaskParent ):

        Task.__init__( self, taskName, True, parent )


    # this function must be overridden
    def processTask(self) -> ETaskResult:
        
        self.error = "RepeatingTask processTask() must be overwritten by derived class"
        return ETaskResult.eFailed

