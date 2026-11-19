
'''
from NewsFeeds import NewsFeeds

from UserInterface import TableWidget

from Tasks import ViewData

from Shared import NewsRssEntry


#
# News Feed URLs Table Widget
#
class NewsFeedUrlsTableWidget( TableWidget ):
    
    TableHeaders = [ "URLs" ]
    
    # init
    def __init__(  self, uiLevel: int ):
        TableWidget.__init__( Defs.   self,uiLevel, self.TableHeaders )
                
 
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
            assert( False )
            
        self.setUpdatesEnabled(True)
    # updateTable



#
# News Feeds Table Widget
#
class NewsFeedTableWidget( TableWidget ):
    
    TableHeaders = NewsFeeds.FIELD_NAMES
        
    # init object
    def __init__(  self, uiLevel: int, headers: list[str]  ):
        TableWidget.__init__( self, uiLevel, headers )
                

    # set table row values
    def __setTableRow__( self, row: int, news: NewsRssEntry ):
                
        columns = [ news.stock, news.title, news.url, news.published, news.summary ]
        for column in columns:
            self.setItem( row, 0, TableWidget.getTextColumnItem( column ) )
              
                    
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.lastDataUpdate.copy( updateData )
        
        row = int(0)
        
        if updateData.isList():

            for news in updateData.dataList:
                self.__setTableRow__( row, news )
                row += 1
            
        else:
            
            keys = updateData.dataDict.keys()
            for key in keys:
                self.__setTableRow__( row, updateData.dataDict[ key ] )
                row += 1    

        self.setUpdatesEnabled(True)



#
# News Feeds Sentiment Table Widget
#
class NewsFeedsSentimentTableWidget( TableWidget ):
    
    TableHeaders = [ "Icon", "Blob Polarity", "Blob Subjectivity", "Report Name", "Title", "Summary" ]
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

# NewsFeedsSentimentTableWidget

'''