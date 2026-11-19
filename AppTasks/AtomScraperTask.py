
import feedparser

from AppDefs import DirDefs
from AppServices import HyperlinkTracker
from AppTasks import BaseScraperTask, NewsScraperTask
from AppBaseTask import TaskParent
from AppUtils import GuardedList 
from FileSystem import FileSystem   



#
# Atom Scraper Task - we search for news about companies
#
class AtomScraperTask( BaseScraperTask ):

    INPUT_DIR       = DirDefs.addToInputDir( "AtomFeeds" )
    INPUT_FILE      = DirDefs.makePath( INPUT_DIR, "AtomFeedUrls.txt" )
    
    FIELD_NAMES     = [ "Title", "Link", "Description", "Published", "Images", "Categories" ]


    def getFieldNames(self) -> list[str]:
        return self.FIELD_NAMES 


    def __init__( self, parent: TaskParent ):

        if not FileSystem.doesDirExist( self.INPUT_DIR ):
            FileSystem.createDir( self.INPUT_DIR )
        
        BaseScraperTask.__init__( self, "AtomScraper", parent, self.FIELD_NAMES, self.INPUT_FILE )

        self.sleepTimeout       = int(1)
        self.savedUrls          = GuardedList()
        
        BaseScraperTask.readInputFile( self )
    
        self.__startTask__()


    # process our task
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

        feedData    = feedparser.parse( url )   # type: ignore

        rssHyperlinks: list[str] = []

        for rssEntry in feedData.entries:       # type: ignore
            rssHyperlinks.append( rssEntry.linkUrl ) # type: ignore

        cleansedHyperlinks = HyperlinkTracker.cleanseHyperlinks( rssHyperlinks ) # type: ignore
        
        for hyperlink in cleansedHyperlinks:
            NewsScraperTask.appendOtherHyperlink( hyperlink )


