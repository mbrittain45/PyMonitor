
'''

from ValueInvesting import BookValue
from UserInterface import TableWidget
from Tasks import ViewData



#
# RSS Feeds Table Widget
#
class BookValuesTableWidget( TableWidget ):
    
    TableHeaders = [ 'Stock Symbol', 'Current Price', 'Book Value', 'Percent Difference' ]

    # init
    def __init__(  self, uiLevel: int, title: str ):

        TableWidget.__init__( self,uiLevel, self.TableHeaders )
        self.setWindowTitle( title )
                
 
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.lastDataUpdate.copy( updateData )
        
        row = int(0)
        
        for bookValue in updateData.dataList:

            self.setItem( row, 0, TableWidget.getTextColumnItem( bookValue.stockSymbol ) )
            self.setItem( row, 1, TableWidget.getTextColumnItem( bookValue.currentPrice ) )
            self.setItem( row, 2, TableWidget.getTextColumnItem( bookValue.curBookValue ) )
            self.setItem( row, 2, TableWidget.getTextColumnItem( bookValue.getPercentDifference() ) )

            row += 1

        self.setUpdatesEnabled(True)

    


    
    '''