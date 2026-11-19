

# pylint: disable=no-name-in-module
from PySide6.QtCore import QSize, QRect, QMargins
from PySide6.QtWidgets import QTabWidget

from App import theStockApp, StockAppWindow


#
# Stock App Abbreviated API functions
#
class AppAbbrvApi:


    @staticmethod
    def getGeometry( uilevel: int ) -> QRect:
        return theStockApp.getMainWindow().getWindowGeometry( uilevel )


    @staticmethod
    def getMargin() -> QMargins:
        return theStockApp.getMainWindow().getWindowMargin()


    @staticmethod
    def getButtonMargin() -> QMargins:
        return theStockApp.getMainWindow().getButtonMargin()


    @staticmethod
    def getGeoSize( uilevel: int ) -> QSize:
        return theStockApp.getMainWindow().getWindowGeometry( uilevel ).size()


    @staticmethod
    def getMainWnd() -> StockAppWindow:
        return theStockApp.getMainWindow()


    @staticmethod
    def getMainWidget() -> QTabWidget:
        return theStockApp.getMainWindow().getMainWidget()
 
    
    @staticmethod
    def getMainWidgetTabNames():

        tabNames: list[str] = [ AppAbbrvApi.getMainWidget().tabText(i) for i in range( AppAbbrvApi.getMainWidget().count() ) ] # type: ignore
        return tabNames

