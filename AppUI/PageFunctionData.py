

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget

from AppUtils import GuardedList


#
# Specify the page functionlity that is enabled
#
class PageFunctionData:

    def __init__( self, parent: QWidget, pageName: str, uilevel: int, colHdrs: list[str] ):

        self.parent         = parent
        self.pageName       = pageName
        self.uilevel        = uilevel
        self.columnHeaders  = GuardedList()
        self.columnHeaders.appendList( colHdrs )

        self.pageDeletable  = True
        self.pageHideable   = True
        self.pageUpdateable = True

        self.rowDeletable   = False
        self.rowHideable    = False
        self.rowUpdateable  = False
        self.rowReordering  = False
        self.rowHasPage     = False
        self.rowPageNames   = [ ]

        self.columnDeletable  = False
        self.columnHideable   = False
        self.columnUpdateable = False
        self.columnReordering = False
        self.editableColumns: list[int]  = [ ]


