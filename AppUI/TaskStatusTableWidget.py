


'''

from PySide6.QtCore import QTimer, SLOT

from App import theApp, Defs, ViewUpdate
from AppTasks.BaseTask import Task, TaskState
from AppTasks.TaskUtils import FunctionPtrTask
from AppUI import TableWidget 
from AppUtils import DTUtils


#
# Task Table Widget - display task statistics
#             
class TaskTableWidget( TableWidget ):

    # TASK_VIEW_FIELD_NAMES = [ "UID", "Name", "State", "Previous State", "Next State", "Next Runtime", "Result", "Error" ]
    
    
    def __init__(  self, uiLevel: int ):
        TableWidget.__init__( self, Defs.EViewType.eTaskStatus, uiLevel, Task.TASK_VIEW_FIELD_NAMES )
        FunctionPtrTask( "DisplayTasks", self, self.displayTasks )


    def __startTimer__(self, timeout = int(5000) ):
        nextWakeupTime = (DTUtils.getCurTime() + DTUtils.getMsecTimeDelta( self._sleepTimeout ))
        QTimer.singleShot( nextWakeupTime, self, SLOT('timerCallback()') )
        

    # our timer callback function, when our wait timeout elapses this gets called and we restart ourself
    def timerCallback(self):
        FunctionPtrTask( "DisplayTasks", self, self.displayTasks )
        

    def displayTasks( self ):

        activeTasks = theApp.getTaskMgr().copyAllTasks()

        self.setUpdatesEnabled(False)
        
        self.clear()

        row      = int(0)
        taskKeys = activeTasks.getKeys()
        for key in taskKeys:
            self.__displayTask__( row, activeTasks[ key ] )
            row += 1

        self.setUpdatesEnabled(True)

        # start timer to redisplay in 5 seconds if active view; 15 secs otherwise
        if theApp.getActiveView() == Defs.EViewType.eTaskStatus:
            self.__startTimer__()
        else:
            self.__startTimer__( int(15000) )

    
    def __displayTask__( self, row: int, task: Task ):
        
        self.setItem( row, 0, TableWidget.getTableWidgetItem( task.getTaskId() ) )
        self.setItem( row, 1, TableWidget.getTableWidgetItem( task.getTaskName() ) )
        self.setItem( row, 2, TableWidget.getTableWidgetItem( TaskState.taskStateToString( task.getState() ) ) )
        self.setItem( row, 3, TableWidget.getTableWidgetItem( TaskState.stateToString( task.getPrevState() ) ) )
        self.setItem( row, 4, TableWidget.getTableWidgetItem( TaskState.stateToString( task.getNextState() ) ) )
        self.setItem( row, 5, TableWidget.getTableWidgetItem( task.getNextRuntime() ) )
        self.setItem( row, 6, TableWidget.getTableWidgetItem( task.getResult() ) )
        self.setItem( row, 7, TableWidget.getTableWidgetItem( task.getError() ) )


    def updateTable( self, updateData: ViewUpdate ):
        assert( updateData.isDict() )
        # nothing to do here since we get our data from the TaskMgr every update


    def taskComplete( self, task ):
        del task
        task = None



        


'''