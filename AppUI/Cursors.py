


'''

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

from enum import Enum

from App import theApp


#
# cursor types as a enum
#
class ECursorType( Enum ):

    eArrow      = 0
    eSizeVer    = 1
    eUpArrow    = 2
    eSizeHor    = 3
    eCross      = 4
    eSizeBDiag  = 5
    eIBeam      = 6
    eSizeFDiag  = 7
    eWait       = 8
    eSizeAll    = 9
    eBusy       = 10
    eSplitVer   = 11
    eForbidden  = 12
    eSplitHor   = 13
    ePointing   = 14
    eOpenHand   = 15
    eWhatsThis  = 16
    eClosedHand = 17
    eDragMove   = 18
    eDragCopy   = 19
    eDragLink   = 20

   
# todo: how and when to use -- like drag and drop is easy, what else is needed ?

#
# Takes care of cursor changes
#
class Cursor:

    # the cursors
    Cursors = [ Qt.ArrowCursor, Qt.SizeVerCursor, Qt.UpArrowCursor, Qt.SizeHorCursor, Qt.CrossCursor, Qt.SizeBDiagCursor,
                Qt.IBeamCursor, Qt.SizeFDiagCursor, Qt.WaitCursor, Qt.SizeAllCursor, Qt.BusyCursor, Qt.SplitVCursor,
                Qt.ForbiddenCursor, Qt.SplitHCursor, Qt.PointingHandCursor, Qt.OpenHandCursor, Qt.WhatsThisCursor,
                Qt.ClosedHandCursor, Qt.DragMoveCursor, Qt.DragCopyCursor, Qt.DragLinkCursor ]

    @staticmethod
    def getCursor( eCursorType ):
        return Cursor.Cursors[ eCursorType ]

    @staticmethod
    def overrideCursor( eCursorType ):
        theApp.setOverrideCursor( QCursor( Cursor.Cursors[ eCursorType ] ) )

    @staticmethod
    def restoreCursor():
        theApp.restoreOverrideCursor()

    @staticmethod
    def setCursor( eCursorType ):
        theApp.setCursor( QCursor( Cursor.Cursors[ eCursorType ] ) )

    @staticmethod
    def setPos(screen, p):
        theApp.getCursor().setPos( screen, p )

    @staticmethod
    def setXYPos(screen, x, y ):
        theApp.getCursor().setPos( screen, x, y )


'''