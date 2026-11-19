

# pylint: disable=no-name-in-module
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QPushButton, QTableWidgetItem, QWidget, QLabel

from AppServices import AppAbbrvApi


#
# Simple Widget - creates simple widgets
#
class SimpleWidget:



    @staticmethod
    def createLabel( text: str, parent: QWidget ) -> QLabel:

        label = QLabel( parent )
        label.setObjectName( text )
        label.setGeometry(QRect(80, 830, 63, 20))
        
        return label



    # get table widget item - column item
    @staticmethod
    def createTableItem( text: str, colNum: int, editableColumns: list[int] ) -> QTableWidgetItem:

        item = QTableWidgetItem( text )
                
        flagVal = item.flags()
        
        if colNum in editableColumns:
            flagVal += int( Qt.ItemFlag.ItemIsSelectable )      # type: ignore
            flagVal += int( Qt.ItemFlag.ItemIsEditable )        # type: ignore
            item.setFlags( item.flags() + flagVal )             # type: ignore

        return item
    



    # get a push button
    @staticmethod
    def createPushButton( text: str, parentWidget: QWidget, objectName: str ):

        button = QPushButton( text, parentWidget )
        button.setObjectName( objectName )
        button.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        return button


            