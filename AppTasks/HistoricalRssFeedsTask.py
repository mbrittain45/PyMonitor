

'''

import os

from Services.Utilities import TimeUtils, FileOps
from Services.Tasks import Task, EBaseTaskState, ETaskResult
from Services.Topics.RssFeeds import RssFeeds


class HistoricalRssFeedsTask( Task ):
    
    def __init__( self, searchData ):
        Task.__init__( self, "HistoricalRssFeedsTask" )
        self._histSearchData = searchData
        self._timer.start( 5 )
        self._results = []


    # read lines from a historical file
    def __readHistoricalFile__( self, date ):
        historicalFile = RssFeeds.RSS_OUT_FILE.format( date )
        if os.path.exists( historicalFile ):
            return FileOps.readLines( historicalFile )
        return []


    # task run thread function
    def processTask(self) -> bool:

        # read all the rss feed files from the start date to the end date
        # and search the feed data for stock name and symbol. Then output
        # all found feeds that are related.
        searchDate = self._histSearchData.startDate 
        while ( searchDate < self._histSearchData.endDate ):
        
            flines = self._parent.readHistoricalFile( searchDate )
            for fline in flines:
                    
                pos = fline.find( self._histSearchData.stockName )
                if pos != -1:
                    self._results.append( fline )
                    continue
                    
                pos = flines.find( self._histSearchData.symbol )
                if pos != -1:
                    self._results.append( fline )
            
            # increment the historical date
            searchDate = TimeUtils.incrementDate( searchDate )
            
        # write out the results
        if len( self._results ) > 0:
            FileOps.writeLines( self._histSearchData.outputFile, self._results )

        # we only run once so we are completed
        self.state = EBaseTaskState.eComplete
        
        return True



'''
