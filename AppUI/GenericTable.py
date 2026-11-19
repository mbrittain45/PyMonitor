

# pylint: disable=no-name-in-module
from PySide6.QtCore import QRect 
from PySide6.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QAbstractItemView, QHeaderView

from AppServices import AppAbbrvApi
from AppUI import PageFunctionData, GenericTableRow, GenericTableColumn, BasePage



#
# Generic Table
#
class GenericTable( BasePage ):


    # get the column size
    def __getColumnSize__(self, calcColumnSize: float, columnHdr: str ):
        if (len( columnHdr ) + 1) > calcColumnSize:
            return (len( columnHdr ) + 1)
        return calcColumnSize
    
    
    # size the table columns
    def __sizeColumns__( self ):
        
        numCols         = self.funcData.columnHeaders.getCount()
        column          = int(0)
        columnSize      = int(0)
        totalSize       = int( self.tableWidget.geometry().width() )
        calcColumnSize  = float(int( totalSize ) / int(numCols))
        
        columnList      = self.funcData.columnHeaders.copyList()
        for columnHdr in columnList:
            columnSize  = self.__getColumnSize__( calcColumnSize, columnHdr )
       
            self.tableWidget.horizontalHeader().setSectionResizeMode( column, QHeaderView.ResizeMode.Stretch )
            self.tableWidget.horizontalHeader().resizeSection( column, int(columnSize) )
            
            column          += 1
            totalSize       -= columnSize
            if columnSize > calcColumnSize:       
                calcColumnSize = (totalSize / (numCols - column))
   

    # init 
    def __init__( self, funcData: PageFunctionData ):
        BasePage.__init__( self, funcData )
        
        self.rows    = GenericTableRow( self )
        self.columns = GenericTableColumn( self )



    # add the table widget
    def addTableWidget(self):

        self.verticalLayoutWidget = QWidget( self )
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget2")
        self.verticalLayoutWidget.setGeometry( QRect(210, 60, 1031, 701) )

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout2")
        self.verticalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        #self.setGeometry( AppAbbrvApi.getGeometry().getMainWindow().getWindowGeometry( uiLevel )  )
        self.tableWidget.setContentsMargins( AppAbbrvApi.getMargin() )
        self.tableWidget.setSelectionMode( QAbstractItemView.SelectionMode.SingleSelection )
        self.tableWidget.setSelectionBehavior( QAbstractItemView.SelectionBehavior.SelectRows )
        # todo: self.tableWidget.setEditTriggers( QAbstractItemView.NoEditTriggers ) 
        self.tableWidget.setColumnCount( self.funcData.columnHeaders.getCount() )
        self.tableWidget.setHorizontalHeaderLabels( self.funcData.columnHeaders.copyList() )
        self.tableWidget.horizontalHeader().setSectionsMovable(True)

 
        self.__sizeColumns__()
   
        self.rows.addTableRows()
        self.columns.addTableColumns()

