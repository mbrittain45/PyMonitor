

from AppBaseTask import Task, ETaskResult

from AppBaseTask.TaskState import TaskParent

from AppUtils import GuardedQueue #, Logger

from FileSystem import FileOperation, AsyncFileTask


#
# Async File Task Manager - we manage the ASyncFileTasks
# 
class AsyncFileTaskMgr( Task, TaskParent ): 

    FileOpQueue          = GuardedQueue()

    def __init__( self, parent: TaskParent ):

        Task.__init__( self, "AsyncFileTaskMgr", True, parent )

        self.sleepTimeout   = int(1)
        self.suspend        = False


    @staticmethod
    def requestFileOp( fileOp: FileOperation ) -> bool:

        if fileOp.isValid():
            AsyncFileTaskMgr.FileOpQueue.addItem( fileOp )    # type: ignore
            return True
        else:
            fileOp.parent.fileOpComplete( fileOp )
            return False
        

    def processTask(self) -> bool: # type: ignore
    
        if self.suspend:
            return True

        if self.FileOpQueue.getCount() > 0:

            while self.FileOpQueue.getCount() > 0:

                AsyncFileTask( self.FileOpQueue.getHead(), self )

        return True



    def taskComplete( self, task: Task ):

        if task.result != ETaskResult.eSucceeded:
            #Logger.error( f"AsyncFileTask failed performing a FileOperation: {task.fileOp.getOpAsStr()} on File: {task.fileOp.filepath} - error: {task.result" )
            
            task.errorCnt += 1
            if task.errorCnt < 2:
                
                # rerun the task if its the first error
                task.__startTask__()
                return

        del task    # clean up the task


