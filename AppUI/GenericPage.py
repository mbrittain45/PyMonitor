

# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, QRect
from PySide6.QtWidgets import QVBoxLayout, QWidget

from typing import Any

from AppUI import PageUpdateTask, PageFunctionData, GenericInputDlg, GenericTable, SimpleWidget
from AppUtils import GuardedList, GuardedDictionaryList
from AppDefs import ViewData, ViewUser
from AppServices import AppAbbrvApi


# the global update task
gPageUpdateTask = PageUpdateTask()


#
# Generic Page
#
class GenericPage( GenericTable, ViewUser ):
    
    gUpdateQueue        = GuardedDictionaryList()
    
    # init the page
    def __init__( self, funcData: PageFunctionData ):

        self.tableData = ViewData( funcData.pageName, self )

        GenericTable.__init__( self, funcData )

        self.table.cellChanged.connect( self.onCellChanged ) # type: ignore


    # add Page Buttosn vertical layout
    def addPageButtons( self ):

        self.verticalLayoutWidget = QWidget( self )
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry( QRect(20, 80, 121, 591) )
        
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        self.allocatePageButtons()
        pageButtons = [ self.savePageButton, self.delPageButton, self.hidePageButton, self.updatePageButton, self.restoreDelPageButton, self.restoreHidPageButton, self.customPageButton ]
                
        for pageButton in pageButtons:
            self.verticalLayout.addWidget( pageButton )



    # display page names and get a page name selection from the user
    def displayPageNames( self, title: str, pageNames: list[str] ) -> str:

        genDlg = GenericInputDlg( title, "Choose Page:", True, pageNames )
        return genDlg.displayDialog()


    # when using this function the head value must be unique like a UID
    @staticmethod
    def updateSingleRow( pageName: str, rowData: list[str] ) -> None:
        
        glist = GuardedList()
        glist.appendList( rowData )
        
        GenericPage.gUpdateQueue.addItem( pageName, glist )



    # when using this function the head value must be unique like a UID
    def updateRowWithData( self, rowData: list[str] ) -> None:

        row = 0
        searchValue: str = rowData[ row ]
        while row < self.tableWidget.rowCount():
            item = self.tableWidget.item( row, 0 ) 
            if item:
                if item.text() == searchValue:
                    column = 0
                    for data in rowData:
                        self.tableWidget.setItem( row, column, SimpleWidget.createTableItem( data, column, self.funcData.editableColumns ) )
                        column += 1
                    return # were done    
            row += 1
            

    # called to update the entire table        
    def updatePageData( self, updateData: ViewData ) -> None:

        self.tableData.deepCopy( updateData )
        self.setUpdatesEnabled(False)       
        self.tableWidget.clear()
        
        row = 0
        tableKeys = self.tableData.dictData.getKeys() # type: ignore
        for key in tableKeys:
            
            col = 0
            items: list[Any] = self.tableData.dictData.getItems( key )   # type: ignore
            for item in items:  # type: ignore
                self.baseTable.setItem( row, col, self.getColumnItem( item, col in self.funcData.editableColumns ) )   # type: ignore
                col += 1
            row += 1           
        else:
            assert( False )
            
        self.setUpdatesEnabled(True)



    # should never be called off of our copy of the view data
    def viewDataChanged( self, viewData: ViewData ) -> None:    # type: ignore
        # todo:
        assert( False )
 

    # PAGE specific slot functions
            
    @Slot()
    def updatePage( self ):
        assert( False ) # todo:


    @Slot()
    def savePage( self ):
        self.tableData.owner.viewDataChanged( self.tableData )  # type: ignore
        self.savePageButton.setEnabled( False )



    @Slot()
    def deletePage( self ):
        AppAbbrvApi.getMainWnd().deletePage( AppAbbrvApi.getMainWidget().currentIndex() )


    @Slot()
    def restoreDeletedPage( self ):

        pageNames = AppAbbrvApi.getMainWnd().getDeletedPages()
        if len( pageNames ) > 0:
            pageName = self.displayPageNames( "Restore Deleted Page", pageNames )
            if len( pageName ) > 0:
                AppAbbrvApi.getMainWnd().restoreDeletedPage( pageName )


    @Slot()
    def hidePage( self ):
        AppAbbrvApi.getMainWnd().hidePage( AppAbbrvApi.getMainWidget().currentIndex() )


    @Slot()
    def restoreHiddenPage( self ):
        pageNames = AppAbbrvApi.getMainWnd().getHiddenPages()
        if len( pageNames ) > 0:
            pageName = self.displayPageNames( "Restore Hidden Page", pageNames )
            if len( pageName ) > 0:
                AppAbbrvApi.getMainWnd().restoreHiddenPage( pageName )


    @Slot()
    def onCellChanged(self, row: int, column: int ) -> None:
        self.savePageButton.setEnabled( True )
        colItem = self.tableWidget.item( row, column ) 
        self.tableData.dictData.tableDataChanged( row, column, colItem.text() ) # type: ignore


    @Slot()
    def addCustomCode( self ):
        assert( False )

        # todo: add custom code to the processing of data on this page


    @Slot()
    def createCustomPage( self ):
        assert( False )
        # todo: allow the user to create a page and the task that feeds the page data
        
        # get the page name

        # create the page

        # define the columns of the table

        # define the what the row recrods will be data format and where the data is coming from

        # where to get the data from

        # how to process the data in a new task






    def allocatePageButtons( self ):

        self.savePageButton = SimpleWidget.createPushButton( "Save Page", AppAbbrvApi.getMainWidget(), "savepage" )
        self.savePageButton.clicked.connect( self.savePage )  
        self.savePageButton.setEnabled(False)

        self.delPageButton = SimpleWidget.createPushButton( "Delete Page", AppAbbrvApi.getMainWidget(), "deletepage" )
        self.delPageButton.clicked.connect( self.deletePage )  
        self.delPageButton.setEnabled( True )

        self.hidePageButton = SimpleWidget.createPushButton( "Hide Page", AppAbbrvApi.getMainWidget(), "hidepage" )
        self.hidePageButton.clicked.connect( self.hidePage )  
        self.hidePageButton.setEnabled( True )

        self.updatePageButton = SimpleWidget.createPushButton( "Update Page", AppAbbrvApi.getMainWidget(), "updatepage" )
        self.updatePageButton.clicked.connect( self.updatePage )  
        self.updatePageButton.setEnabled( True )

        self.restoreDelPageButton = SimpleWidget.createPushButton( "Restore Deleted Page", AppAbbrvApi.getMainWidget(), "restoredeletepage" )
        self.restoreDelPageButton.clicked.connect( self.restoreDeletedPage )  
        self.restoreDelPageButton.setEnabled( False )

        self.restoreHidPageButton = SimpleWidget.createPushButton( "Restore Hidden Page", AppAbbrvApi.getMainWidget(), "restorehiddenpage" )
        self.restoreHidPageButton.clicked.connect( self.restoreHiddenPage )  
        self.restoreHidPageButton.setEnabled( False )

        self.customPageButton = SimpleWidget.createPushButton( "Create Custom Page", AppAbbrvApi.getMainWidget(), "createcustompage" )
        self.customPageButton.clicked.connect( self.createCustomPage )  
        self.customPageButton.setEnabled( True )

        self.customCodeButton = SimpleWidget.createPushButton( "Add Custom Code", AppAbbrvApi.getMainWidget(), "addcustomcode" )
        self.customCodeButton.clicked.connect( self.addCustomCode )  
        self.customCodeButton.setEnabled( True )

