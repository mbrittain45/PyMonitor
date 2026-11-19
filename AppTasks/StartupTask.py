

'''

from enum import Enum

from Tasks import Task, ETaskResult
from RssFeeds import RssFeeds



#
# Application Object Types
#
class EObject( Enum ):
    
    eRSSFeeds                   = 0    
    eHistoricalRSSFeeds         = 1    
    eNewsFeeds                  = 2
    eHistoricalNewsFeeds        = 3   
    
    eAllStocks                  = 4   
    eStockSummaries             = 5   
    eHistoricalSummaries        = 6  
    eStockPrices                = 7   
    eHistoricalStockPrices      = 8   
    eMonitoredStocks            = 9   
    eHistoricalMonitoredStocks  = 10   
    
    eAllETFs                    = 11   
    eETFSummaries               = 12   
    eHistoricalETFSummaries     = 13  
    eETFPrices                  = 14   
    eHistoricalETFPrices        = 15   
    eMonitoredETFs              = 16   
    eHistoricalMonitoredETFs    = 17   



#
# Startup Task - our startup task which allocates all the application objects
#
class StartupTask( Task ):
    
    def __init__( self, threadMgr ):
        Task.__init__( self, "StartupTask" )
        self._threadMgr = threadMgr
        

    # our callback slot is not use as we never start our timer we are just start immediately
    def timerCallbackSlot(self):
        assert( False )
    
    # process the task
    def processTask(self) -> bool:
       
        self._threadMgr.objects[ EObject.eRSSFeeds ]                  = RssFeeds()    
        
        #self._threadMgr.objects[ EObject.eNewsFeeds ]                 = NewsFeeds(w)   
        
        #self._threadMgr.objects[ EObject.eAllStocks ]                  = AllStocks( ".\\Data\\Output\\AllListedUSStocks_{}.dat".format( TimeUtils.getYear() ) )   
        #self._threadMgr.objects[ EObject.eStockSummaries ]            = StockSummaries()   
        #self._threadMgr.objects[ EObject.eStockPrices ]               = StockPrices()   
        #self._threadMgr.objects[ EObject.eMonitoredStocks ]           = MonitoredStocks( ".\\Data\\Input\\MonitoredStocks.dat" )   
        
        #self._threadMgr.objects[ EObject.eAllETFs ]                   = AllETFs( ".\\Data\\Output\\AllUSETFs_{}.dat".format( TimeUtils.getYear() ) )   
        #self._threadMgr.objects[ EObject.eETFSummaries ]              = ETFSummaries()   
        #self._threadMgr.objects[ EObject.eETFPrices ]                 = ETFPrices()   
        #self._threadMgr.objects[ EObject.eMonitoredETFs ]             = MonitoredETFs( ".\\Data\\Input\\MonitoredETFs.dat" )   
        
        
        #self._threadMgr.objects[ EObject.eHistoricalRSSFeeds ]         = HistoricalRssFeeds( ".\\Data\\Input\\HistoricalRssFeeds.dat" )    
        #self._threadMgr.objects[ EObject.eHistoricalNewsFeeds ]       = HistoricalNewsFeeds( ".\\Data\\Input\\HistoricalNewsFeeds.dat" )   
        
        #self._threadMgr.objects[ EObject.eHistoricalSummaries ]       = HistoricalSummaries()  
        #self._threadMgr.objects[ EObject.eHistoricalStockPrices ]     = HistoricalStockPrices()   
        #self._threadMgr.objects[ EObject.eHistoricalMonitoredStocks ] = HistoricalMonitoredStocks()   
        
        #self._threadMgr.objects[ EObject.eHistoricalETFSummaries ]    = HistoricalETFSummaries()  
        #self._threadMgr.objects[ EObject.eHistoricalETFPrices ]       = HistoricalETFPrices()   
        #self._threadMgr.objects[ EObject.eHistoricalMonitoredETFs ]   = HistoricalMonitoredETFs()   
        
        return True
        

'''