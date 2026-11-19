


# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, QRect 
from PySide6.QtWidgets import QHBoxLayout, QWidget

from AppServices import AppAbbrvApi
from AppUI import SimpleWidget, GenericTable, TableColumnTracker



#
# Generic Table Column - functionality
#
class GenericTableColumn:


    def __init__( self, parent: GenericTable ):

        self.columnTracker     = TableColumnTracker()
        self.parent = parent
        

    # Column Buttons horizontal layout
    def addTableColumns(self):

        self.horizontalLayoutWidget = QWidget( self.parent )
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget2")
        self.horizontalLayoutWidget.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout2")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )
        
        if self.parent.funcData.columnDeletable:

            button = SimpleWidget.createPushButton( "Delete Column", self.horizontalLayoutWidget, "deleteColumnButton" )
            button.clicked.connect( self.deleteColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Deleted Column", self.horizontalLayoutWidget, "restoreDeletedColumnButton" )
            button.clicked.connect( self.restoreDeletedColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.parent.funcData.columnHideable:

            button = SimpleWidget.createPushButton( "Hide Column", self.horizontalLayoutWidget, "hideColumnButton" )
            button.clicked.connect( self.hideColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Column", self.horizontalLayoutWidget, "restoreHiddenColumnButton" )
            button.clicked.connect( self.restoreHiddenColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.parent.funcData.columnReordering:
            self.parent.tableWidget.horizontalHeader().sectionMoved.connect( self.reorderColumns )

        #if self.columnUpdateable = False
        #self.columnReordering = False


    
    # figure out new column reordering don't allow row zero to move
    def reorderColumns( self ):

        column_count = self.parent.tableWidget.columnCount()
        column_names: list[str] = []
        for i in range(column_count):
            header_item = self.parent.tableWidget.horizontalHeaderItem(i)
            if header_item is not None:
                column_names.append(header_item.text())
            else:
                column_names.append(str(i + 1)) # Default header names are usually just the column index + 1
        

    # COLUMN Slots
    
    @Slot()
    def deleteColumn( self ):
        self.columnTracker.delete( self.parent.tableWidget )


    @Slot()
    def restoreDeletedColumn( self ):

        deletedCols = self.columnTracker.getDeleted()
        if len( deletedCols ) > 0:
            colName = self.parent.displayNames( "Restore Column", "Choose Column to Restore:", deletedCols )
            if len( colName ) > 0:
                self.columnTracker.restoreDeleted( colName, self.parent.tableWidget, self.parent.funcData )


    @Slot()
    def hideColumn( self ):
        self.columnTracker.hide( self.parent.tableWidget )


    @Slot()
    def restoreHiddenColumn( self ):

        hiddenCols = self.columnTracker.getHidden()
        if len( hiddenCols ) > 0:
            colName = self.parent.displayNames( "Restore Column", "Choose Column to Restore:", hiddenCols )
            if len( colName ) > 0:
                self.columnTracker.restoreHidden( colName, self.parent.tableWidget, self.parent.funcData )


#    @Slot
#    def updateColumn( self ):
    



'''
# Enable section moving for the whole header
self.tableWidget.horizontalHeader().setSectionsMovable(True)

# Connect the signal
self.tableWidget.horizontalHeader().sectionMoved.connect(self.keep_column_zero_fixed)

def keep_column_zero_fixed(self, logicalIndex, oldVisualIndex, newVisualIndex):
    # If the column being moved is column 0 OR a column was moved into position 0
    if oldVisualIndex == 0 or newVisualIndex == 0:
        # Block signals to prevent an infinite recursion loop
        self.tableWidget.horizontalHeader().blockSignals(True)
        
        # Move the section back to where it belongs
        # moveSection(visualIndex_from, visualIndex_to)
        self.tableWidget.horizontalHeader().moveSection(newVisualIndex, oldVisualIndex)
        
        self.tableWidget.horizontalHeader().blockSignals(False)
'''

   
