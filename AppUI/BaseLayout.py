

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget, QLayout

from App.main import theStockApp


#        
# The QBoxLayout class lines up widgets horizontally or vertically. 
# QHBoxLayout and QVBoxLayout are convenience subclasses of QBoxLayout. 
# QGridLayout lays out widgets in cells by dividing the available space into rows and columns. 
# QFormLayout, on the other hand, sets its children in a two-column form with labels in the left column and input fields in the right column.
#


#
# Base Layout 
#
class BaseLayout( QLayout ):

    def __init__(self, uiLevel: int ):

        QLayout.__init__(self)

        self.setGeometry( theStockApp.getMainWindow().getWindowGeometry( uiLevel )  )
        self.setContentsMargins( theStockApp.getMainWindow().getWindowMargin() )



#
# Base Widget
#
class Widget( QWidget ):
    
    def __init__(self, uiLevel: int ):

        QWidget.__init__(self)

        self.setGeometry( theStockApp.getMainWindow().getWindowGeometry( uiLevel )  )
        self.setContentsMargins( theStockApp.getMainWindow().getWindowMargin() )

