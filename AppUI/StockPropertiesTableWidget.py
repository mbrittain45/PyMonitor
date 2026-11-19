

'''


from PySide6.QtCore import Slot

from PySide6.QtWidgets import QTableWidgetItem

from Application import Stock, theApp

from Definitions import EField, STOCK_FIELD_NAMES

from UserInterface import TableWidget, ValueEditBox, ValueEditBoxParent
    
from Tasks import ViewData


#
# Stock Properties Table Widget - display a stocks values and allow for notes and some field value changes
#             
class StockPropsTableWidget( TableWidget, ValueEditBoxParent ):

    
    # constructor    
    def __init__(  self, uiLevel: int, fields: list[EField], stock: Stock ):
        
        self._fields  = fields
        self._stock   = stock
        self._dlg     = None
        self._uiLevel = uiLevel
        self._selectFld  = int(-1)
        
        fldNames = [ "Stock Property Type", "Stock Property Value" ]
        TableWidget.__init__( self, uiLevel, fldNames )
    
        self.__populateTable__()
        
        self.itemClicked.connect( self.rowItemClicked )
        self.itemDoubleClicked.connect( self.rowItemDoubleClicked )

        
    # set task table row data
    def __populateTable__( self ):

        row = int( 0 )
        for fld in self._fields:
            self.setItem( row, 0, TableWidget.getTableWidgetItem( STOCK_FIELD_NAMES[ int(fld) ] ) )
            self.setItem( row, 1, TableWidget.getTableWidgetItem( self._stock.data[ fld ] ) )
            row += 1
        

    # allow changing of a stock's property value
    def __displayChangeFieldDlg__( self, row: int ):
        
        self._selectFld = row
        self._dlg       = ValueEditBox( (self._uiLevel - 2), self, self._stock.data[ row ] )
        self._dlg.show()
         
        
    # value edit box is complete so set the new value
    def setValueEditBoxComplete( self, text: str ):
        
        if len( text ) > 0:
            self._stock.data[ self._selectFld ] = text
        self._dlg.close()
        


    # update the table
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        self.__populateTable__()
        self.setUpdatesEnabled(True)



    # row item clicked see if data value is changeable
    @Slot(QTableWidgetItem)
    def rowItemClicked(self, item):

        row = item.row()
        if Stock.isFieldModifiable( self._fields[ row ] ):
            self.__displayChangeFieldDlg__( row )
        else:
            theApp.getLogger().logInfo( "Stock Property Field: '{}' Clicked but Property is not modifiable".format( STOCK_FIELD_NAMES[ int(self._fields[ row ]) ]  ) )



    # row item double clicked display the stocks properties
    @Slot(QTableWidgetItem)
    def rowItemDoubleClicked(self, item):
        
        row = item.row()
        if Stock.isFieldModifiable( self._fields[ row ] ):
            self.__displayChangeFieldDlg__( row )
        else:
            theApp.getLogger().logInfo( "Stock Property Field: '{}' Double Clicked but Property is not modifiable".format( STOCK_FIELD_NAMES[ int(self._fields[ row ]) ]  ) )



'''