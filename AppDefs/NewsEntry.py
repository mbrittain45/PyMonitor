

from AppDefs import Defs
from AppUtils import HtmlParser
from AppServices import AppIndexer, HyperlinkTracker
from AppUtils import GuardedList


#
# News Entry
#
class NewsEntry:
        
    # init ourself default constructor
    def __init__(self, title: str, url: str, summary: str ): 
    
        self.title          = title
        self.url            = url
        self.summary        = summary
        self.storyPath      = ""
        self.uid            = AppIndexer.getNewsEntryIndex()
        self.sentimentScore = int(-1)
        self.company        = ""
        self.published      = ""

        self.miningMatches  = GuardedList()


    # format ourself
    def fileFormat( self ) -> str:

        line = (self.company + Defs.COMDEL + self.title + Defs.COMDEL + self.url + Defs.COMDEL)
        line += (self.summary + Defs.COMDEL + self.storyFilePath + Defs.COMDEL)
        line += f"{self.sentimentScore}"
        line += self.published
        line += "\n"
        
        return line

    
    # parse a file line containing our info
    def parseFormat( self, fileLine: str ) -> None:
        
        values  = fileLine.split( Defs.COMDEL )
        
        self.company        = values[0]
        self.title          = values[1]
        self.url            = values[2]
        self.summary        = values[3]
        self.storyFilePath  = values[4]
        self.sentimentScore = values[5]
        self.published      = values[6]
    

    # find new hyperlinks
    @staticmethod
    def findNewHyperlinks( htmlResp: str ) -> list[str]:

        hyperlinks    = HtmlParser.parseAllHyperlinks( htmlResp )           # type: ignore
        newHyperlinks = HyperlinkTracker.cleanseHyperlinks( hyperlinks )    # type: ignore
        return newHyperlinks                                                # type: ignore

    

    # create a news entry
    @staticmethod
    def createNewsEntry( url: str, respHtml: str ):
      
        title   = HtmlParser.parseTitle( respHtml )
        summary = HtmlParser.parseSummary( respHtml )
        published = HtmlParser.parsePublishDate( respHtml )

        entry = NewsEntry( title, url, summary )
        entry.published = published

        return entry


