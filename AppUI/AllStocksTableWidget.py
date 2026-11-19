
#from Application import EField

#from Definitions import STOCK_FIELD_NAMES
#from UserInterface import TableWidget

''' todo:

import ReadDailyAllStocksCSVFile


#
# Table Widget for RequestAllStocks
#
class RequestAllStocksTableWidget( TableWidget ):
    
    # init the object
    def __init__( self, uiLevel: int ):
        TableWidget.__init__( self, uiLevel, STOCK_FIELD_NAMES )
    
            
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        
        self.clear()
        row = int(0)
        
        if updateData.isDictionary():
            
            keys = updateData.dataDict.keys()
            for key in keys:
                stock = updateData.dataDict[ key ]
                for field in EField:
                    self.setItem( row, int(field), TableWidget.getTableWidgetItem( stock.data[ int(field) ] ) )

                row += 1
        else:
            assert( False )
            
        self.setUpdatesEnabled(True)



#
# Table Widget for RequestAllStocks New Found Stocks
#
class RequestAllStocksNewStocksTableWidget( TableWidget ):
    
    # init the object
    def __init__( self, uiLevel: int ):
        TableWidget.__init__( self, uiLevel, STOCK_FIELD_NAMES )
    
            
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        
        self.clear()
        row = int(0)
        
        if updateData.isDictionary():
            
            keys = updateData.dataDict.keys()
            for key in keys:
                stock = updateData.dataDict[ key ]
                for field in EField:
                    self.setItem( row, int(field), TableWidget.getTableWidgetItem( stock.data[ int(field) ] ) )

                row += 1
    
        else:
            assert( False )
        
        self.setUpdatesEnabled(True)



#
# Table Widget for ReadAllStocksCSV
#
class ReadAllStocksCSVTableWidget( TableWidget ):
    
    # init the object
    def __init__( self, uiLevel: int ):
        TableWidget.__init__( self, uiLevel, ReadDailyAllStocksCSVFile.INPUT_FILE_HEADERS )
    
            
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        
        self.clear()
        row = int(0)
        
        if updateData.isDictionary():
            
            keys = updateData.dataDict.keys()
            for key in keys:
                stock = updateData.dataDict[ key ]
                for field in ReadDailyAllStocksCSVFile.DATA_FIELDS:
                    self.setItem( row, int(field), TableWidget.getTableWidgetItem( stock.data[ int(field) ] ) )

                row += 1
        
        else:
            assert( False )
        
        self.setUpdatesEnabled(True)
        



#
# Table Widget for ReadAllStocksCSV New Stocks
#
class ReadAllStocksCSVNewTableWidget( TableWidget ):
    
    # init the object
    def __init__( self, uiLevel: int ):
        TableWidget.__init__( self, uiLevel, ReadDailyAllStocksCSVFile.INPUT_FILE_HEADERS )
    
            
    # update the table with values
    def updateTable( self, updateData: ViewData ):
        
        self.setUpdatesEnabled(False)
        
        self.clear()
        row = int(0)
        
        if updateData.isDictionary():
            
            keys = updateData.dataDict.keys()
            for key in keys:
                stock = updateData.dataDict[ key ]
                for field in ReadDailyAllStocksCSVFile.DATA_FIELDS:
                    self.setItem( row, int(field), TableWidget.getTableWidgetItem( stock.data[ int(field) ] ) )

                row += 1
        
        else:
            assert( False )
        
        self.setUpdatesEnabled(True)
        

        '''