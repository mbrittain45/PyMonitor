

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidget

from AppUI import SimpleWidget, PageFunctionData
from AppUtils import GuardedDictionaryList


#
# Table Row Tracker - track hidden and deleted rows
#
class TableRowTracker:


    def __init__( self ):
        self.hiddenRows     = GuardedDictionaryList()
        self.deletedRows    = GuardedDictionaryList()
  

    def getListData( self, table: QTableWidget ) -> list[str]:

        rowIndex = table.currentRow()
        rowData: list[str] = []

        for column in range(table.columnCount()):
            item = table.item( rowIndex, column )
            if item is not None:
                rowData.append( item.text() )
            else:
                rowData.append("") 

        return rowData

    
    def hide( self, table: QTableWidget ):
        rowData = self.getListData( table )
        self.hiddenRows.addItem( (rowData[0] + " - " + rowData[1]), rowData )
        table.removeRow( table.currentRow() )


    def delete( self, table: QTableWidget ):
        rowData = self.getListData( table )
        self.deletedRows.addItem( (rowData[0] + " - " + rowData[1]), rowData )
        table.removeRow( table.currentRow() )


    def getHidden( self ):
        return self.hiddenRows.getKeys()


    def getDeleted( self ):
        return self.deletedRows.getKeys()


    def restore( self, rowItems: list[str], table: QTableWidget, funcData: PageFunctionData ):
    
        col = 0
        row = table.rowCount();
        table.insertRow(row);
        for item in rowItems:
            table.setItem( row, col, SimpleWidget.createTableItem( item, col, funcData.editableColumns ) )
            col += 1


    def restoreHidden( self, rowKey: str, table: QTableWidget, funcData: PageFunctionData ):
        rowItems: list[str] = self.hiddenRows.getItems( rowKey )
        if rowItems:
            self.restore( rowItems, table, funcData )
      

    def restoreDeleted( self, rowKey: str, table: QTableWidget, funcData: PageFunctionData ):
        rowItems: list[str] = self.hiddenRows.getItems( rowKey )
        if rowItems:
            self.restore( rowItems, table, funcData )




#
# Table Column Tracker - track hidden and deleted rows and columns and other UI functionality
#
class TableColumnTracker:


    def __init__( self ):
        self.hiddenColumns  = GuardedDictionaryList()
        self.deletedColumns = GuardedDictionaryList()


    def getListData( self, table: QTableWidget ) -> list[str]:

        columnData: list[str] = []

        for row in range(table.rowCount()):
            item = table.item( row, table.currentColumn() )
            if item is not None:
                columnData.append( item.text() )
            else:
                columnData.append("") 

        return columnData


    def hide( self, table: QTableWidget ):
        columnData = self.getListData( table )
        hdrItem = table.horizontalHeaderItem( table.currentColumn() )
        if hdrItem:
            self.hiddenColumns.addItem( hdrItem.text(), columnData )
        table.removeColumn( table.currentColumn() )


    def delete( self, table: QTableWidget ):
        columnData = self.getListData( table )
        hdrItem = table.horizontalHeaderItem( table.currentColumn() )
        if hdrItem:
            self.deletedColumns.addItem( hdrItem.text(), columnData )
        table.removeColumn( table.currentColumn() )


    def getHidden( self ) -> list[str]:
        return self.hiddenColumns.getKeys()


    def getDeleted( self ) -> list[str]:
        return self.deletedColumns.getKeys()
        

    def restore( self, columnItems: list[str], table: QTableWidget, funcData: PageFunctionData ) -> None:
        row = 0
        colCnt = table.columnCount()
        table.insertColumn( colCnt );
        for item in columnItems:
            table.setItem( row, colCnt, SimpleWidget.createTableItem( item, colCnt, funcData.editableColumns ) )
            row += 1


    def restoreHidden( self, colKey: str, table: QTableWidget, funcData: PageFunctionData ) -> None:
        colItems: list[str] = self.hiddenColumns.getItems( colKey )
        if colItems:
            self.restore( colItems, table, funcData )
      

    def restoreDeleted( self, colKey: str, table: QTableWidget, funcData: PageFunctionData ) -> None:
        colItems: list[str] = self.hiddenColumns.getItems( colKey )
        if colItems:
            self.restore( colItems, table, funcData )



   


        