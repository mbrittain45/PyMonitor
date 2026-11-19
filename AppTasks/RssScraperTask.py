
import feedparser


from AppDefs import DirDefs
from AppServices import HyperlinkTracker
from AppTasks import BaseScraperTask, NewsScraperTask
from AppBaseTask import TaskParent
from AppUtils import GuardedList 
from FileSystem import FileSystem   



#
# Rss Scraper Task - we search for news about companies
#
class RssScraperTask( BaseScraperTask ):

    INPUT_DIR       = DirDefs.addToInputDir( "RssFeeds" )
    INPUT_FILE      = DirDefs.makePath( INPUT_DIR, "RssFeedUrls.txt" )
    
    FIELD_NAMES     = [ "Title", "Link", "Description", "Published", "Images", "Categories" ]
    PAGE_NAME       = "RSS URLS"

    def getFieldNames(self) -> list[str]:
        return self.FIELD_NAMES 


    def __init__( self, parent: TaskParent ):

        if not FileSystem.doesDirExist( self.INPUT_DIR ):
            FileSystem.createDir( self.INPUT_DIR )
        
        BaseScraperTask.__init__( self, "RssScraper", parent, self.FIELD_NAMES, self.INPUT_FILE )

        self.sleepTimeout       = int(2)
        self.savedUrls          = GuardedList()
        
        self.__startTask__()


    
    def processTask(self) -> bool:

        self.checkFileMonitor()

        if self.urls.getCount():

            url = self.urls.popHead()
            self.savedUrls.addItem( url )
            self.performRequest( url )

        else:

            self.urls.appendList( self.savedUrls.copyList() )
            self.savedUrls.clearList()

        return True



    # perform a url request
    def performRequest( self, url: str ) -> None:

        feedData    = feedparser.parse( url )       # type: ignore

        rssHyperlinks: list[str] = []
        for rssEntry in feedData.entries:            # type: ignore  
            rssHyperlinks.append( rssEntry.linkUrl ) # type: ignore

        cleansedHyperlinks = HyperlinkTracker.cleanseHyperlinks( rssHyperlinks ) # type: ignore
        
        for hyperlink in cleansedHyperlinks:
            NewsScraperTask.appendOtherHyperlink( hyperlink )

