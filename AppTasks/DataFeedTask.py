

'''
import os 

from datetime import datetime

from Application import theApp

from Definitions import EViewType

from Tasks import Task, EBaseTaskState

from Shared import FileOps, TimeUtils, NewsRssEntry, ViewData


#
# BaseDataFeedsTask - base tsak for all data feed type tasks
#
class BaseDataFeedsTask( Task ):
    
     
    def __init__(self, taskName: str, parent: any, urls: list[str] ):
        
        Task.__init__( self, taskName )
        
        self._parent            = parent
        
        self._urls              = []
        self._lastUrlReqTimes   = []
        self._backupUrls        = []
        self._otherTasks        = []
        self._newEntries        = []
        
        self.setTaskUrls( urls )
       
            
    # set new urls to request
    def setTaskUrls( self, urls: list[str] ):
        
        # clear last request times
        self._lastUrlReqTimes.clear()
        
        # set last request times to epoch
        Len   = len( urls )
        index = int(0)
        while index < Len: 
            self._lastUrlReqTimes.append( Epocher.getTime() )
            index += 1
            
        
        # set the new urls depending on whether we are running or not
        if self.state == EBaseTaskState.eRunning:
            self._backupUrls.copy( urls )
            theApp.getTaskMgr().restartTaskWhenDone( self )
        else:
            self._urls.clear()
            self._urls.copy( urls )
            self._timer.start( 5 )
                
    

    # compute time delta for a given url index
    def __computeTimeRange__(self, urlIndex: int ):
        return datetime.now() - self._lastUrlReqTimes[ urlIndex ]
    

    
    # process new rss feed entries
    def __processEntries__( self, urlIndex: int, entries: list[NewsRssEntry] ):
        
        timeRange = self.__computeTimeRange__( urlIndex )
        for entry in entries:
        
            entryTime = datetime.strptime( entry.published, "%a, %d %b %Y %H:%M:%S %z")
            if (datetime.now() - entryTime) <= timeRange:
                self._newEntries.append( entry )
            
    

    # update our displays
    def __updateViews__(self, urlViewType: EViewType, dataViewType: EViewType ):
        
        # display our urls
        theApp.getTaskMgr().updateView( ViewListUpdate( urlViewType, self._urls ) )
        # display our news entries
        theApp.getTaskMgr().updateView( ViewListUpdate( dataViewType, self._newEntries ) )
           
        
        
    # if our urls got updated while we were running..load them now
    def __checkBackupUrls__( self ):
        
        if len( self._backupUrls ) > 0:
            self._urls.clear()
            self._urls.copy( self._backupUrls )
            self._backupUrls.clear()
        
    

            '''