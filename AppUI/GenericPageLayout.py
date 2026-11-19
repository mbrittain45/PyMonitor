
'''
# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, QRect 
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QTableWidget, QVBoxLayout, QWidget, QAbstractItemView, QHeaderView

from AppServices import AppAbbrvApi
from AppUI import PageFunctionData, SimpleWidget, BasePage



#
# Generic Page Layout
#
class GenericPageLayout( BasePage ):


  

    # init 
    def __init__( self, funcData: PageFunctionData ):

        BasePage.__init__( self, funcData )
        
        # Table Widget vertical layout
        self.verticalLayoutWidget_2 = QWidget( AppAbbrvApi.getMainWidget() )
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry( QRect(210, 60, 1031, 701) )

        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        self.tableWidget = QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)

        #self.setGeometry( AppAbbrvApi.getGeometry().getMainWindow().getWindowGeometry( uiLevel )  )
        self.tableWidget.setContentsMargins( AppAbbrvApi.getMargin() )
        self.tableWidget.setSelectionMode( QAbstractItemView.SelectionMode.SingleSelection )
        self.tableWidget.setSelectionBehavior( QAbstractItemView.SelectionBehavior.SelectRows )
        # todo: self.tableWidget.setEditTriggers( QAbstractItemView.NoEditTriggers ) 
        self.tableWidget.setColumnCount( self.funcData.columnHeaders.getCount() )
        self.tableWidget.setHorizontalHeaderLabels( self.funcData.columnHeaders.copyList() )
        self.tableWidget.horizontalHeader().setSectionsMovable(True)

        if self.funcData.columnReordering:
            self.tableWidget.horizontalHeader().sectionMoved.connect( self.reorderColumns )
 
        self.__sizeColumns__()
   
        # Row Buttons horizontal layout
        self.horizontalLayoutWidget = QWidget( AppAbbrvApi.getMainWidget() )
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        # Table Row buttons
        if funcData.rowDeletable:
            button = SimpleWidget.createPushButton( "Delete Row", self.horizontalLayoutWidget, "deleteRowButton" ) 
            button.clicked.connect( self.deleteRow )
            self.horizontalLayout.addWidget( button ) 
            button.setEnabled( True )
            
            button = SimpleWidget.createPushButton( "Restore Delete Row", self.horizontalLayoutWidget, "restoreDeletedRowButton" )
            button.clicked.connect( self.restoreDeletedRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if funcData.rowHideable:
            button = SimpleWidget.createPushButton( "Hide Row", self.horizontalLayoutWidget, "hideRowButton" )
            button.clicked.connect( self.hideRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Row", self.horizontalLayoutWidget, "restoreHiddenRowButton" )
            button.clicked.connect( self.restoreHiddenRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )
            
        if funcData.rowUpdateable:
            button = SimpleWidget.createPushButton( "Update Row", self.horizontalLayoutWidget, "updateRowButton" )
            button.clicked.connect( self.updateRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        #if funcData.rowReordering:
        #    vlayout.theLayout.addWidget( self.getPushButton( "Reorder Row", uilevel, self.reorderRowCB ) ) # type: ignore

        if funcData.rowHasPage:
            button = SimpleWidget.createPushButton( "View Row Page", self.horizontalLayoutWidget, "viewRowPageButton" )
            button.clicked.connect( self.viewRowPage )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

  
        # Column Buttons horizontal layout
        self.horizontalLayoutWidget2 = QWidget( AppAbbrvApi.getMainWidget() )
        self.horizontalLayoutWidget2.setObjectName(u"horizontalLayoutWidget2")
        self.horizontalLayoutWidget2.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout2")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )
        
        if self.funcData.columnDeletable:
            button = SimpleWidget.createPushButton( "Delete Column", self.horizontalLayoutWidget, "deleteColumnButton" )
            button.clicked.connect( self.deleteColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Deleted Column", self.horizontalLayoutWidget, "restoreDeletedColumnButton" )
            button.clicked.connect( self.restoreDeletedColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.funcData.columnHideable:
            button = SimpleWidget.createPushButton( "Hide Column", self.horizontalLayoutWidget, "hideColumnButton" )
            button.clicked.connect( self.hideColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Column", self.horizontalLayoutWidget, "restoreHiddenColumnButton" )
            button.clicked.connect( self.restoreHiddenColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        #if self.columnUpdateable = False
        #self.columnReordering = False

        SimpleWidget.createLabel( "Row Buttons", self )
        SimpleWidget.createLabel( "Column Buttons", self )

        self.show()

 '''