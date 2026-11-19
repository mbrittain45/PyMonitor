

# pylint: disable=no-name-in-module
from PySide6.QtCore import QRect
#from PySide6.QtWidgets import QMenuBar      #, QMenu, QFileDialog, QPlainTextEdit # QVBoxLayout, QWidget, QLabel,

from App import EFontType, StockAppWindow, theStockApp


#
# Stock Menu Bar Menus:    Application  View  Statistics  Search
#               
class StockAppMenuBar:


    def __init__( self, mainWnd: StockAppWindow, menuGeometry: QRect ):

        self.menuBar = mainWnd.menuBar()
        self.mainWnd = mainWnd
 
        self.menuBar.setObjectName("menubar")
        self.menuBar.setFont( theStockApp.getFont( EFontType.eMenuFont ) )
        self.menuBar.setGeometry( menuGeometry ) 


''' todo:

        self.__createAppMenu__()
        self.__createViewMenu__()
        self.__createStatsMenu__()
        

    # create a menu action and everything that goes along w/ it
    def createAction( self, text: str, shortcut: str, slotFunc: Callable[] ) -> QAction:    # type: ignore
         
        action = QAction( self.mainWnd )
        action.setObjectName( text )
        action.setText( text )
        if len( shortcut ) > 0:
            action.setShortcut( shortcut )
        action.triggered.connect( slotFunc )
        return action


    # create the application menu
    def __createAppMenu__(self):
        
        appMenu = self.menuBar.addMenu( "Application" )
        appMenu.addAction( self.createAction( "Open File", "ctrl+o", self.openFileAction ) )
        appMenu.addSeparator()
        appMenu.addAction( self.createAction( "Exit App", "ctrl+x", self.exitAppAction ) )


    # create view menu
    def __createViewMenu__(self):

        viewMenu = self.menuBar.addMenu( "View" )
        
        viewMenu.addAction( self.createAction( "Find View", "ctrl+v", self.findViewAction ) )
        viewMenu.addAction( self.createAction( "Clear View", "ctrl+l", self.clearViewAction ) )
        viewMenu.addSeparator()
        viewMenu.addAction( self.createAction( "Reset View", "ctrl+r", self.resetViewAction ) )
        viewMenu.addAction( self.createAction( "Reset Views", "ctrl+s", self.resetViewsAction ) )


    # create the statistics menu
    def __createStatsMenu__( self ):
        
        statsMenu = self.menuBar.addMenu( "Stats" )

        statsMenu.addAction( self.createAction( "Find Stock", "ctrl+s", self.findStockAction ) )
        

        



    # let the user pick a page name they want to see
    pageNames: list[str] = theStockApp.getMainWindow().getPageNames()


    # Slots for QActions    
            
    # exit the application
    def onExitApplication( self ):
        theApp.exitApp()
        

    # open an external file for the user
    def onOpenFile( self ):

        dialog = QFileDialog(self)
        dialog.setFileMode( QFileDialog.AnyFile )
        dialog.setNameFilter( "*.txt" )

        # Connect the fileSelected signal to our callback
        dialog.fileSelected.connect( self.handleFileSelected )

        
    # handle when a file is selected via QFileDialog
    def handleFileSelected( self, fileName ):

        if fileName:
            self.openFileForViewing( fileName )
    
    #def onTaskStatusesView( self ):

'''