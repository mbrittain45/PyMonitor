

from AppDefs import DirDefs, Defs, NewsEntry
from AppServices import HyperlinkTracker
from AppBaseTask import TaskParent
from AppTasks import BaseScraperTask
from AppUtils import DTFmt, GuardedList, GuardedQueue, TimeInsensitiveRequestUrl
from FileSystem import FileOperation, FileSystem



#
# New Scraper Task - we search for news about companies
#
class NewsScraperTask( BaseScraperTask ):

    INPUT_DIR       = DirDefs.addToInputDir( "News" )
    INPUT_FILE      = DirDefs.makePath( INPUT_DIR, "NewsSiteUrls.txt" )

    OUTPUT_DIR      = DirDefs.addToCacheDir( "News" )
    OUTPUT_FILE     = DirDefs.makePath( OUTPUT_DIR, "News_{}.dat" )

    STORY_DIR       = DirDefs.makePath( OUTPUT_DIR, "Stories_" )
    
    FIELD_NAMES     = [ "Stock", "Title", "Link", "Summary", "StoryFileName" ]

    otherHyperlinks = GuardedQueue()        
     

    def getFieldNames(self) -> list[str]:
        return self.FIELD_NAMES 


    def __init__( self, parent: TaskParent ):

        FileSystem.createDir( self.INPUT_DIR )
        FileSystem.createDir( self.OUTPUT_DIR )
        self.storyDir = (self.STORY_DIR + DTFmt.getMonthYear())
        FileSystem.createDir( self.storyDir )
        self.storyFileBase = (self.storyDir + "NewsStory_")    
        
        BaseScraperTask.__init__( self, "NewsScraper", parent, self.FIELD_NAMES, self.INPUT_FILE )

        self.sleepTimeout       = int(1)
        self.scanCount          = int(0)
        self.newNewsEntries     = GuardedList()
        self.savedNewsEntries   = GuardedList()
        self.savedUrls          = GuardedList()

        self.readInputFile()
    
        self.__startTask__()


    @staticmethod
    def appendOtherHyperlink( url: str ) -> None:
        NewsScraperTask.otherHyperlinks.addTail( url )


    # write a news story summary to a file by news entry uid
    def writeStoryFile( self, newsEntry: NewsEntry ) -> NewsEntry:

        newsEntry.storyPath = (self.storyFileBase + f"{newsEntry.uid}" + Defs.DATEXT)
        FileOperation.createWriteBlobFileOp( newsEntry.storyPath, newsEntry.summary, self, False )
        return newsEntry


    # process our task
    def processTask(self) -> bool:

        self.checkFileMonitor()
        
        remainder = self.scanCount % 3

        match remainder:

            case 0:
                
                # request our urls
                if self.urls.getCount():
                    url = self.urls.popHead()
                    self.savedUrls.addItem( url )
                    self.performRequest( url )
                else:
                    self.urls.appendList( self.savedUrls.copyList() )
                    self.savedUrls.clearList()

            case 1:

                # request our found hyperlinks
                if self.hyperlinks.getCount():
                    url = self.hyperlinks.popHead()
                    if self.performRequest( url ):
                        HyperlinkTracker.addHyperlink( url ) # type: ignore

            
            case 2:

                # request other found hyperlinks
                if self.otherHyperlinks.getCount():
                    url = self.otherHyperlinks.popHead()
                    if self.performRequest( url ):
                        HyperlinkTracker.addHyperlink( url ) # type: ignore
                        
            case _:

                assert( False )

        self.scanCount += 1

        if self.scanCount % 10 == 0:
            self.saveNewsEntries()

        return True

        
    # perform a url request
    def performRequest( self, url: str ) -> bool:

        data_tuple = TimeInsensitiveRequestUrl.get( url )            # type: ignore
            
        # make sure ther request succeeded
        if data_tuple[0]:

            # search for hyperlinks
            newHyperlinks = NewsEntry.findNewHyperlinks( data_tuple[1] )       # type: ignore

            # cleanse the hyperlinks
            cleansedHyperlinks = HyperlinkTracker.cleanseHyperlinks( newHyperlinks )

            # save the cleansed hyperlinks
            self.hyperlinks.appendList( cleansedHyperlinks )                  # type: ignore

            # create the news entry
            newsEntry = NewsEntry.createNewsEntry( url, data_tuple[1] )     # type: ignore

            # write out the summary of the story
            newsEntry = self.writeStoryFile( newsEntry )                    # type: ignore
                
            # save the news entry
            self.newNewsEntries.addItem( newsEntry )

        return data_tuple[0]



    # write our all our news entries
    def saveNewsEntries( self ) -> None:
     
        fmtStr = ""
        
        for newsentry in self.newNewsEntries:        # type: ignore
           
            fmtStr += newsentry.fileFormat()                    # type: ignore
            self.savedNewsEntries.addItem( newsentry )          # type: ignore

            NewsMiningTask.queueNewsEntry( newsentry )          # type: ignore

        FileOperation.createReadBlobFileOp( self.OUTPUT_FILE.format( DTFmt.getDate() ), self, False )

'''
    
  