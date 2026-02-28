

import time
import threading


from PySide6.QtCore import QThreadPool, QMutexLocker, QMutex, QTimer

from enum import Enum

from AppUtils import GuardedList, GuardedDictionaryList, GuardedDictionary

from AppBaseTask import TaskParent, Task

from AppTasks import AllStocksTask #, AllETFsTask, PreferredStocksTask, WatchdogTask, NewsTask, RssTask, NewsMiningTask, RssMiningTask
        



#
# Task Manager - creates and owns the managed tasks for all to use and starts 
#           all other tasks on the thread pool
#
class TaskManager( TaskParent ):

    # sleep time while checking if the Apop is still paused
    APP_PAUSED_SLEEP = int(5000)

    # init ourself
    def __init__(self):
        
        QThreadPool.setMaxThreadCount( 64 )
        
        self.tasksToStart       = GuardedList()
        
        self.pausedTimerLock    = threading.Lock()
        self.pausedTimerActive  = False

        self.systemTasks        = GuardedDictionary()
        self.viewUpdateQueue    = GuardedDictionaryList()
        self.tasksMutex         = QMutex()
        
        # start the system tasks and they will start the other tasks
        AllStocksTask( self )
        
        #AllETFsTask( self )
        #PreferredStocksTask( self )


#        self.systemTasks.addItem( ESystemTask.eWatchdogTask, WatchdogTask() )
#        self.systemTasks.addItem( ESystemTask.eNewsTask, NewsTask() )
#        self.systemTasks.addItem( ESystemTask.eRssTask, RssTask() )
#        self.systemTasks.addItem( ESystemTask.eNewsTask, NewsMiningTask() )
#        self.systemTasks.addItem( ESystemTask.eRssTask, RssMiningTask() )
        #self._systemTasks.append( WatchdogTask( self ) )
        #self._systemTasks.append( NewsFeedTask( self ) )
        #self._systemTasks.append( RssFeedTask( self ) )
        #self._systemTasks.append( HistoricalTask( self ) )
        #self._systemTasks.append( NewsMiningTask( self ) )
        #self._systemTasks.append( ProcessMiningResultsTask( self ) )
        #self._systemTasks.append( OTCStockTask( self ) )
        #self._systemTasks.append( SearchArchivesTask( self ) )
        #self._systemTasks.append( GetFinancialsTask( self ) )


#    eNewsMiningTask     = int(6)   # start a mining task to search for gold in the news entries
#    eDataMiningTask     = int(7)   # data mining task for sentiment analysis and other data processing for each different task
#    eHistoricalTask     = int(8)   # historical search task
#    eSearchTask         = int(9)   # search our data task
#    eFinancialTask      = int(10)   # read financial statements
#    eStatisticsTask     = int(11)   # statistics for interested companies
#    eMonitoringTask     = int(12)  # monitor a small group of stocks or etfs watching for prices moves
#    eBookValueTask      = int(13)  # search for value companies
#    eShortSqueezeTask   = int(14)  # search for short squeeze companies w/ large short positions
#    eBestWeekTask       = int(15)  # search for compaines having the best week
#    eBestMonthTask      = int(16)  # search for comapines having the best month


        
       #RepeatingFuncPtrTask( "ViewUpdateFuncTask", self, int(1), self.updateViewsTaskFunc )


'''
    # called when one of our tasks is finished
    def taskComplete( self, task: Task ) -> None:

        if task.taskName == "AllStocksTask":
            self.systemTasks.addItem( "NewsTask", NewsTask() )

            


"AllStocksTask"



    def getWatchdogTask( self ):
        return self._systemTasks[ int(ESystemTask.eWatchdogTask) ]

    def getNewsMiningTask(self):
        return self._systemTasks[ int(ESystemTask.eNewsMiningTask) ]

    def getMiningResultsTask(self):
        return self._systemTasks[ int(ESystemTask.eProcMiningTask) ]

    def getSystemTask(self, sysTask: ESystemTask ):
        #if sysTask > ESystemTask.eViewUpdate_Task and sysTask < ESystemTask.eMax_Task:
        return self._systemTasks[ int( sysTask ) ]
        #else:
        #    assert( False )
        #return None 
    

    def getAllActiveTasks(self) -> dict[Task]:
        return self._activeTasks.getCopy()


    def unregisterTask( self, task: Task ):

        Log.info( "Unregistering Task: {} with ID: {}".format( task.getName(), task.getUid() ) )
        with QMutexLocker( self._tasksMutex ):

            checkTask = self._activeTasks.getItem( task.getUID() )
            if checkTask == None:
                Log.error( "TaskManager - runregisterTask called with unknown task: {} : {} - id: {}".format( task.getName(), task.getTaskId(), id(task) ) )
                return 

            removedTask = self._activeTasks.popItem( task.getUID() )
            if removedTask != None:
                removedTask.setRegistered( False )
            else:
                assert(removedTask != None)


    def checkIfAppStillPaused( self ):

        if theApp.isAppPaused():
            
            with self._pausedTimerLock:
                self._pausedTimerActive = True
                QTimer.singleShot( self.APP_PAUSED_SLEEP_TIME, self, self.checkIfAppStillPaused )
        
        else:
            
            with self._pausedTimerLock:
                self._pausedTimerActive = False

            # start all the task that need starting
            for task in self._tasksToStart:
                self.startTask( task )
            
            # clear the task to start list
            self._tasksToStart.clear()



    def startTask( self, task ):

        # see if the app is paused iuf it is don't start anymore tasks until its running again
        if theApp.isAppPaused():

            # we'll start the task when the app is unpaused
            self._tasksToStart.append( task )

            # see if the timer is active, if not start it
            with self._pausedTimerLock:
                if not self._pausedTimerActive:
                    self._pausedTimerActive = True
                    QTimer.singleShot( self.APP_PAUSED_SLEEP_TIME, self, self.checkIfAppStillPaused )

            return  # we are done here

        # make sure the task is registered with us
        if not task.isRegistered():

            Log.info( "Registering Task: {} : {} with OBJ-ID: {}".format( task.getName(), task.getTaskId(), id(task) ) )
            registeredTask = self._activeTasks.getItem( task.getUID() )
            if registeredTask == None:
                self._activeTasks.addItem( task.getUID(), task )
                task.setRegistered( True )
            
        # log a note
        Log.info( "Put Task: {} UID: {} Runtime ID: {} - on the Thread Pool".format( task.getName(), task.getUID(), id(task) ) )
        
        # put the task on the thread pool
        QThreadPool.globalInstance().start( task )
 
        

    def findTask(self, partialName: str ):

        retTasks    = []
        ourTasks    = self._activeTasks.getCopy()
        for task in ourTasks:
            if task.getName().find( partialName ) != -1:
                retTasks.append( task )
        return retTasks

    
    def taskComplete( self, task: Task ):
        
        if task.isRepeating():
            self.startTask( task )
        else:
            del task
            task = None


    @staticmethod
    def waitForTask( task ):
        while not task.isTaskFinished():
            time.sleep( .50 )


    @staticmethod
    def awaitForTasks( tasks = [] ):
        for task in tasks:
            TaskManager.waitForTask( task )

                                
    def updateView( self, viewUpdate: ViewUpdate ):
        self._viewUpdateQueue.addItem( viewUpdate.eViewType, viewUpdate )


    def updateViewsTaskFunc( self ):

        viewKeys = self._viewUpdateQueue.getKeys()
        for viewKey in viewKeys:
           
            updateList = self._viewUpdateQueue.getItem( viewKey )
            if updateList.count() > 0:
                theApp.getWnd().getChildWindow( viewKey ).update( updateList )
                                    
        


#
# Application Object Types
#
class EAppObjectType( Enum ):
    
    eMinStockEnumValue          = int(0)
    eHistoricalFeed             = int(3)   
    eStockSummaries             = int(5)   
    eHistoricalSummaries        = int(6)
    eStockPrices                = int(7)
    eHistoricalStockPrices      = int(8)
    eMonitoredStocks            = int(9)   
    eHistoricalMonitoredStocks  = int(10)   
    eBalanceSheets              = int(11)
    eHistoricalBalanceSheets    = int(12)
    eQuarterlyReports           = int(13)
    eHistoricalQuarterlyReports = int(14)
    eStockTrends                = int(15)
    eHistoricalStockTrends      = int(16)
    eStockMovingAverages        = int(17)
   
    # add new values here for stocks
    eMaxStockEnumValue          = int(18)

    
    eMinEtfEnumValue            = int(30)
    eGetAllEtfs                 = eMinEtfEnumValue
    eEtfSummaries               = int(31)   
    eHistoricalEtfSummaries     = int(32)
    eEtfPrices                  = int(33)
    eHistoricalEtfPrices        = int(34)
    eMonitoredEtfs              = int(35)   
    eHistoricalMonitoredEtfs    = int(36)   
    eEtfNAVs                    = int(37)
    eHistoricalNAVs             = int(38)
    eEtfReports                 = int(39)
    eEtfTrends                  = int(41)
    eHistoricalEtfTrends        = int(42)
    eEtfMovingAverages          = int(43)
    # add new values here for etfs
    
    eMaxEtfEnumValue            = int(44)

    #eMaxObjectType              = int()

    self._appObjects.append( HistoricalData() )   
    self._appObjects.append( StockSummaries() )   
    self._appObjects.append( HistoricalSummaries() )
    self._appObjects.append( StockPrices() )
    self._appObjects.append( HistoricalStockPrices() )
    self._appObjects.append( MonitoredStocks() )   
    self._appObjects.append( HistoricalMonitoredStocks() )   
    self._appObjects.append( HistoricalBalanceSheets() )
    self._appObjects.append( HistoricalQuarterlyReports() )
    self._appObjects.append( StockTrends() ) - once a day
    self._appObjects.append( HistoricalStockTrends() )
    self._appObjects.append( StockMovingAverages() ) - once a day

    '''

'''