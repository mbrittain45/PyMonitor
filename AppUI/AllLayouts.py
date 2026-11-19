

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QGraphicsAnchorLayout
from PySide6.QtWidgets import QBoxLayout, QGraphicsGridLayout, QGraphicsLayout, QGraphicsLinearLayout, QStackedLayout

from enum import Enum

from AppServices import AppAbbrvApi 


#
# layout types
#
class ELayoutType( Enum ):

    eQBoxLayout             = int(0)
    eQFormLayout            = int(1)
    eeQGraphicsAnchorLayout = int(2)
    eQGraphicsGridLayout    = int(3)
    eQGraphicsLayout        = int(4)
    eQGraphicsLinearLayout  = int(5)
    eQGridLayout            = int(6)
    eQHBoxLayout            = int(7)
    eQVBoxLayout            = int(8)
    eQStackedLayout         = int(9)


#
# All Layouts in one object
#
class AllLayouts:


    def __init__( self, layout: ELayoutType, uiLevel: int ):

        self.layoutType = layout
        self.level      = uiLevel
        self.theLayout  = None 



    def getLayout( self, direction: QBoxLayout.Direction = QBoxLayout.Direction.LeftToRight ) -> QLayout:

        if self.theLayout:
            return self.theLayout           # type: ignore

        match self.layoutType:

            case ELayoutType.eQBoxLayout:
                self.theLayout = QBoxLayout( direction )
            case ELayoutType.eQFormLayout:
                self.theLayout = QFormLayout()
            case ELayoutType.eeQGraphicsAnchorLayout:
                self.theLayout = QGraphicsAnchorLayout()
            case ELayoutType.eQGraphicsGridLayout:
                self.theLayout = QGraphicsGridLayout()
            case ELayoutType.eQGraphicsLayout:
                self.theLayout = QGraphicsLayout()
            case ELayoutType.eQGraphicsLinearLayout:
                self.theLayout = QGraphicsLinearLayout()
            case ELayoutType.eQGridLayout:
                self.theLayout = QGridLayout()
            case ELayoutType.eQHBoxLayout:
                self.theLayout = QHBoxLayout()
            case ELayoutType.eQVBoxLayout:
                self.theLayout = QVBoxLayout()
            case ELayoutType.eQStackedLayout:
                self.theLayout = QStackedLayout()              
            case _:
                self.theLayout = QLayout()

    
        self.theLayout.setGeometry( AppAbbrvApi.getGeometry( self.level ) )
        
        margins = AppAbbrvApi.getMargin()
        self.theLayout.setContentsMargins( margins.left, margins.top, margins.right, margins.bottom ) # type: ignore
        
        #self.theLayout.setSpacing( 10 )

        return self.theLayout   # type: ignore


