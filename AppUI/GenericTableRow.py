

# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, QRect 
from PySide6.QtWidgets import QHBoxLayout, QWidget


from AppServices import AppAbbrvApi

from AppUI import SimpleWidget, GenericTable, TableRowTracker


#
# Generic Table Row - functionality
#
class GenericTableRow:

    def __init__( self, parent: GenericTable ):

        self.rowTracker     = TableRowTracker()
        self.parent         = parent
    


    def addTableRows(self):

        self.horizontalLayoutWidget = QWidget( self.parent )
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        # Table Row buttons
        if self.parent.funcData.rowDeletable:

            button = SimpleWidget.createPushButton( "Delete Row", self.horizontalLayoutWidget, "deleteRowButton" ) 
            button.clicked.connect( self.deleteRow )
            self.horizontalLayout.addWidget( button ) 
            button.setEnabled( True )
            
            button = SimpleWidget.createPushButton( "Restore Delete Row", self.horizontalLayoutWidget, "restoreDeletedRowButton" )
            button.clicked.connect( self.restoreDeletedRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.parent.funcData.rowHideable:

            button = SimpleWidget.createPushButton( "Hide Row", self.horizontalLayoutWidget, "hideRowButton" )
            button.clicked.connect( self.hideRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Row", self.horizontalLayoutWidget, "restoreHiddenRowButton" )
            button.clicked.connect( self.restoreHiddenRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )
            
        if self.parent.funcData.rowUpdateable:

            button = SimpleWidget.createPushButton( "Update Row", self.horizontalLayoutWidget, "updateRowButton" )
            button.clicked.connect( self.updateRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )


        #if funcData.rowReordering:
        #    vlayout.theLayout.addWidget( self.getPushButton( "Reorder Row", uilevel, self.reorderRowCB ) ) # type: ignore

        if self.parent.funcData.rowHasPage:

            button = SimpleWidget.createPushButton( "View Row Page", self.horizontalLayoutWidget, "viewRowPageButton" )
            button.clicked.connect( self.viewRowPage )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )


  
    @Slot()
    def deleteRow( self ):
        self.rowTracker.delete( self.parent.tableWidget )

    @Slot()
    def restoreDeletedRow( self ):
        deletedRows = self.rowTracker.getDeleted()
        if len( deletedRows ) > 0:
            rowKey = self.parent.displayNames( "Restore Row", "Choose Row to Restore:", deletedRows )
            if len( rowKey ) > 0:
                self.rowTracker.restoreDeleted( rowKey, self.parent.tableWidget, self.parent.funcData )

    @Slot()
    def hideRow( self ):
        self.rowTracker.hide( self.parent.tableWidget )

    @Slot()
    def restoreHiddenRow( self ):
        hiddenRows = self.rowTracker.getHidden()
        if len( hiddenRows ) > 0:
            rowName = self.parent.displayNames( "Restore Row", "Choose Row to Restore:", hiddenRows )
            if len( rowName ) > 0:
                self.rowTracker.restoreHidden( rowName, self.parent.tableWidget, self.parent.funcData )


    @Slot()
    def updateRow( self ):
        assert( False ) # todo:


    @Slot()
    def viewRowPage( self ):
        assert( False ) # todo:

  