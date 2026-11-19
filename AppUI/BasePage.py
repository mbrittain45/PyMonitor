

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget

from abc import ABC, abstractmethod

from AppServices import AppAbbrvApi
from AppDefs import ViewData
from AppUI import PageFunctionData, GenericInputDlg, SimpleWidget



#
# Base Page
#
class BasePage( QWidget, ABC ):

    def __init__( self, funcData: PageFunctionData ):

        QWidget.__init__( self, AppAbbrvApi.getMainWidget() )
        
        self.funcData       = funcData
        self.popupDlg       = None 
        self.setWindowTitle( self.funcData.pageName )

        self.addPageButtons()
        self.addTableWidget()
        SimpleWidget.createLabel( "Row Buttons", self )
        SimpleWidget.createLabel( "Column Buttons", self )

        # display ourself
        self.show()


    @abstractmethod
    def addPageButtons( self ):
        pass

    @abstractmethod
    def addTableWidget( self ):
        pass

   
    # update data - must be overridden
    @abstractmethod
    def updatePageData( self, updateData: ViewData ) -> None:
        pass


    # display page names and get a page name selection from the user
    def displayNames( self, title: str, caption: str, pageNames: list[str] ) -> str:
        genDlg = GenericInputDlg( title, caption, True, pageNames )
        return genDlg.displayDialog()


