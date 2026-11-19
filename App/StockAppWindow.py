

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QMainWindow, QTabWidget, QMenuBar, QWidget, QToolBar, QStatusBar, QVBoxLayout
from PySide6.QtCore import QSize, QRect, QMargins
from PySide6.QtWidgets import QMainWindow

from AppUtils import GuardedList, GuardedDictionary
from App import StockAppMenuBar
from AppUI import BasePage


#
# our Main Window for the application
#
class StockAppWindow( QMainWindow ):

    SUBVAL = 20


    # init
    def __init__(self, qsize: QSize ):
        
        QMainWindow.__init__(self)

        self.hiddenPages    = GuardedDictionary()
        self.deletedPages   = GuardedDictionary()
        self.pages          = GuardedDictionary()

        self.windowRects     = GuardedList()
        self.windowMargin    = QMargins( self.SUBVAL, self.SUBVAL, self.SUBVAL, self.SUBVAL )
        self.buttonMargin    = QMargins( 2, 2, 2, 2 )

        # Setup the Central Widget
        self.mainWidget      = QTabWidget()          # type: ignore
        self.setCentralWidget( self.mainWidget ) # type: ignore

        # Apply a Layout - This is the "magic" that makes the window contents resizable
        self.centralLayout = QVBoxLayout( self.centralWidget ) # type: ignore

        # Set window properties
        self.setWindowTitle("Stock App Main Window")
        self.resize( 1600, 900 )
        self.setMinimumSize( 400, 225 )

        self.__computeWindowSizes__( qsize )

        self.setGeometry( self.windowRects.getItem( 0 ) )
        self.setContentsMargins( self.windowMargin )

        self.ourMenuBar = StockAppMenuBar( self, QRect(0, 0, 1500, (self.SUBVAL * 3) ) )


    # compute windows sizes for the entire app now
    def __computeWindowSizes__( self, qsize: QSize ) -> None:
        
        left                = qsize.left()           # type: ignore
        top                 = qsize.top()            # type: ignore
        width               = qsize.width()          # type: ignore
        height              = qsize.height()         # type: ignore
      
        rect = QRect( left, top, width, height )    # type: ignore
        self.windowRects.addItem( rect )
            
        subtractValue       = self.SUBVAL
        while subtractValue < 300:                  # 20 levels is enough
        
            rect = QRect( left - subtractValue, top - subtractValue, width - subtractValue, height - subtractValue )        # type: ignore
            self.windowRects.addItem( rect )
            subtractValue   += self.SUBVAL
    

    
    def removeTab( self, tab: int ) -> (QWidget| None):

        tabPage = self.mainWidget.widget( tab )
        self.mainWidget.removeTab( tab )
        return tabPage


    def addTab( self, page: BasePage ):

        index = self.mainWidget.addTab( page, page.windowTitle() )
        self.mainWidget.setCurrentIndex(index)


    def hidePage( self, selpage: int ) -> None:

        tabPage = self.mainWidget.removeTab( selpage )
        self.hiddenPages.addItem( tabPage.windowTitle(), tabPage ) # type: ignore
        

    def deletePage( self, selpage: int ) -> None:

        tabPage = self.mainWidget.removeTab( selpage )
        self.deletedPages.addItem( tabPage.windowTitle(), tabPage ) # type: ignore
        

    def getHiddenPages( self ) -> list[str]:

        return self.hiddenPages.getKeys()

    
    def getDeletedPages( self ) -> list[str]:

        return self.deletedPages.getKeys()

    
    def restoreHiddenPage( self, pageName: str ) -> None:

        page = self.hiddenPages.getItem( pageName )
        if page:
            self.addTab( page )


    def restoreDeletedPage( self, pageName: str ) -> None:

        page = self.deletedPages.getItem( pageName )
        if page:
            self.addTab( page )


    def getMenuBar( self ) -> QMenuBar:

        return self.menuBar()


    def getMenuWidget( self ) -> QWidget:

        return self.menuWidget() 


    def addToolbar( self, title: str  ) -> QToolBar:

        return self.addToolBar( title )


    def getStatusBar( self ) -> QStatusBar:

        return self.statusBar()


    def getMainWidget( self ) -> QTabWidget:

        return self.centralWidget() # type: ignore


    def getWindowGeometry( self, uiLevel: int ) -> QRect:

        if uiLevel < self.windowRects.getCount():
            return self.windowRects.getItem( uiLevel )
        return self.windowRects.getItem( self.windowRects.getCount() - 1 )


    def getWindowSize( self, uiLevel: int ) -> QSize:

        if uiLevel < self.windowRects.getCount():
            return self.windowRects.getItem( uiLevel ).size()
        return self.windowRects.getItem( self.windowRects.getCount() - 1 ).size()

       
    def getWindowMargin( self ) -> QMargins:

        return self.windowMargin

    def getButtonMargin( self ) -> QMargins:

        return self.buttonMargin


    def getWindowSpacing( self ):

        return self.SUBVAL



