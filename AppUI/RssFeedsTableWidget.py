

'''
from UserInterface import TableWidget
from DataFeeds.RssFeeds import RssFeeds
from Tasks import ViewData
from Shared import NewsRssEntry



#
# RSS Feeds Table Widget
#
class RssFeedsUrlsTableWidget( TableWidget ):
    
    TableHeaders = [ "URLs" ]
    

    # init
    def __init__(  self, uiLevel: int ):
        TableWidget.__init__( self,uiLevel, self.TableHeaders )
                
 
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.lastDataUpdate.copy( updateData )
        
        row = int(0)
        
        if updateData.isList():
        
            for url in updateData.dataList:
                self.setItem( row, 0, TableWidget.getTextColumnItem( url ) )
                row += 1

        else:
            
            keys = updateData.dataDict.keys()
            for key in keys:
                self.setItem( row, 0, TableWidget.getTextColumnItem( key ) )
                row += 1

        self.setUpdatesEnabled(True)
    # updateTable



#
# RSS Feeds Table Widget
#
class RssFeedsTableWidget( TableWidget ):
    
    TableHeaders = RssFeeds.FIELD_NAMES
    

    # init
    def __init__(  self, uiLevel: int ):
        TableWidget.__init__( self,uiLevel, RssFeeds.FIELD_NAMES )
                
 
    def __setTableRow__(self, row: int, entry: NewsRssEntry ):
        self.setItem( row, 0, TableWidget.getTextColumnItem( entry.title ) )
        self.setItem( row, 1, TableWidget.getTextColumnItem( entry.link ) )
        self.setItem( row, 2, TableWidget.getTextColumnItem( entry.published ) )
        self.setItem( row, 3, TableWidget.getTextColumnItem( entry.summary ) )
     

    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.lastDataUpdate.copy( updateData )
        
        row = int(0)
        
        if updateData.isList():
            for entry in updateData.dataList:
                self.__setTableRow__( row, entry )
                row += 1
        else:
            keys = updateData.dataDict.keys()
            for key in keys:
                self.__setTableRow__( row, updateData.dataDict[key] )
                row += 1
            
        self.setUpdatesEnabled(True)
    # updateTable

# RssFeedsTableWidget



#
# RSS Feeds Sentiment Table Widget
#
class RssFeedsSentimentTableWidget( TableWidget ):
    
    TableHeaders = [ "Icon", "Blob Polarity", "Blob Subjectivity", "Report Name", "Summary" ]
    PlusIcon    = "Plus-Sign.png"
    MinusIcon   = "Minus-Sign.png"
    
    
    # init    
    def __init__(  self, uiLevel: int ):
        TableWidget.__init__( self,uiLevel, self.TableHeaders )
                
 
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.lastDataUpdate.copy( updateData )
        
        row = int(0)
        
        if updateData.isList():
        
            for stockSymbol, rssSummary, sentiment in updateData.dataList:
    
                if sentiment.isPositive():
                    self.setItem( row, 0, TableWidget.getIconColumnItem( self.PlusIcon ) )
                else:
                    self.setItem( row, 0, TableWidget.getIconColumnItem( self.MinusIcon ) )
                    
                self.setItem( row, 1, TableWidget.getTextColumnItem( stockSymbol ) )
                self.setItem( row, 2, TableWidget.getTextColumnItem( sentiment.blob.polarity ) )
                self.setItem( row, 3, TableWidget.getTextColumnItem( sentiment.blob.subjectivity ) )
                self.setItem( row, 4, TableWidget.getTextColumnItem( rssSummary ) )
                self.setItem( row, 5, TableWidget.getTextColumnItem( updateData.reportName ) )
                
                row += 1
           
        else:
            assert( False )

        self.setUpdatesEnabled(True)

# RssFeedsSentimentTableWidget

'''     