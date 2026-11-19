

'''

import os 


from Application import theApp
from Services.Utilities import HistoricalSearchData, FileOps, TimeUtils
from Services.Topics.RssFeeds import HistoricalRssFeedsTask



#
# Historical RSS Feeds
#
class HistoricalRssFeeds:
    
    def __init__(self, fileName ):
        
        self._indexNum      = int(1)
        self._fileName      = fileName
        self._searchData    = HistoricalSearchData()
                
        if os.path.exists( self._fileName ) == False:
            self._searchData.createFile( self._fileName )
        else:
            self._searchData.readFile( self._fileName )    # read the file
            self._searchData.createFile( self._fileName )  # clear the file
                
        theApp.getFileMonitor().addPath( self, self._fileName )

        self.__checkToStartNewTask__()
            

    # see if we should start a new task
    def __checkToStartNewTask__( self ):
        
        if self._searchData.isValid():
            
            FileOps.write( ".\\Data\\Input\\HistoricalRssFeeds-Processing-{}.dat".format( TimeUtils.getFileDT() ), self._searchData.toString() )
            
            newTask = HistoricalRssFeedsTask( self._searchData )
            theApp.getTaskMgr().registerTask( newTask )
        
        else:
        
            FileOps.write( ".\\Data\\Input\\HistoricalRssFeeds-Processing-Error-{}.dat".format( TimeUtils.getFileDT() ), self._searchData.toString() + " - INVALID SEARCH DATA" )
            self.getClient().display( "Invalid Historical Search Data: {}".format( self._searchData.toString() ) )
        


    # callback for file monitor
    def fileChanged( self, fileName ):
        
        if fileName == self._fileName:
             
            self._searchData.readFile( self._fileName )    # read the changed file
            
            self._searchData.createFile( self._fileName )  # clear the file
            self.__checkToStartNewTask__()
        
        else:
            self.getClient().display( "Historical RSS Feeds told to Reload the Wrong File: " + fileName )
    

'''