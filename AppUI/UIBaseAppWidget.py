
'''
from PySide6.QtWidgets import QWidget

from UserInterface import eUIEvent, UIParent


class UIBaseAppWidget( QWidget ):
    
    def __init__( self, parent, descr, name ):
        super().__init__()
    
        self._parent = parent
        self.setAcceptDrops( False )
        self.setAccessibleDescription( descr )
        self.setAccessibleName( name )

        
    # overrides virtuals
        
    # mouse double click
    def mouseDoubleClickEvent( self, e ):

        if self._parent.isProcessingEvent( eUIEvent.eMouseDoubleClick ) == False:
            e.ignore()
            return
        
        self._parent.processEvent( e )


    # mouse move event
    def mouseMoveEvent( self, e ):

        if self._parent.isProcessingEvent( eUIEvent.eMouseMove ) == False:
            e.ignore()
            return

        self._parent.processEvent( e )


    # mouse press event
    def mousePressEvent( self, e ):

        if self._parent.isProcessingEvent( eUIEvent.eMousePress ) == False:
            e.ignore()
            return

        self._parent.processEvent( e )


    # mouse release event
    def mouseReleaseEvent( self, e ):

        if self._parent.isProcessingEvent( eUIEvent.eMouseRelease ) == False:
            e.ignore()
            return

        self._parent.processEvent( e )


    # mouse wheel event
    def wheelEvent( self, e ):

        if self._parent.isProcessingEvent( eUIEvent.eMouseWheel ) == False:
            e.ignore()
            return

        self._parent.processEvent( e )

   

                def actions()
        def addAction()
        def addActions()
        def adjustSize()
                
        def frameGeometry()
        def frameSize()
        def geometry()

        def grab()
        def grabGesture()
        def grabKeyboard()
        def grabMouse()
        def grabShortcut()
        
        def insertAction()
        def insertActions()
        def internalWinId()

        def isActiveWindow()
        def isAncestorOf()
        def isEnabled()
        def isEnabledTo()
        def isFullScreen()
        def isHidden()
        def isLeftToRight()
        def isMaximized()
        def isMinimized()
        def isModal()
        def isRightToLeft()
        def isTopLevel()
        def isVisible()
        def isVisibleTo()
        def isWindow()
        def isWindowModified()

        def layout()
        def layoutDirection()
        def locale()

        def mapFrom()
        def mapFromGlobal()
        def mapFromParent()
        def mapTo()

        def mapToGlobal()
        def mapToParent()
        def mask()
        def maximumHeight()
        def maximumSize()
        def maximumWidth()
        def minimumHeight()
        def minimumSize()
        def minimumWidth()
        
        def move()

        def nativeParentWidget()
        def nextInFocusChain()
        def normalGeometry()
        def overrideWindowFlags()
        def overrideWindowState()
        def palette()
        def parentWidget()
        def pos()
        def previousInFocusChain()
        
        def rect()
        def releaseKeyboard()
        def releaseMouse()
        def releaseShortcut()

        def removeAction()
        def render()
        def repaint()
        def resize()
        def restoreGeometry()
        def saveGeometry()
        def screen()
        def scroll()

        def setAttribute()
        def setAutoFillBackground()
        def setBackgroundRole()
        def setBaseSize()
        def setContentsMargins()
        def setContextMenuPolicy()
        def setCursor()
        def setFixedHeight()
        def setFixedSize()
        def setFixedWidth()
        def setFocus()
        def setFocusPolicy()
        def setFocusProxy()
        def setFont()
        def setForegroundRole()
        def setGeometry()
        def setGraphicsEffect()
        def setInputMethodHints()
        def setLayout()
        def setLayoutDirection()
        def setLocale()
        def setMask()
        def setMaximumHeight()
        def setMaximumSize()
        def setMaximumWidth()
        def setMinimumHeight()
        def setMinimumSize()
        def setMinimumWidth()
        def setMouseTracking()
        def setPalette()
        def setParent()
        def setScreen()
        def setShortcutAutoRepeat()
        def setShortcutEnabled()
        def setSizeIncrement()
        def setSizePolicy()
        def setStatusTip()
        def setStyle()
        def setTabletTracking()
        def setToolTip()
        def setToolTipDuration()
        def setUpdatesEnabled()
        def setWhatsThis()
        def setWindowFilePath()
        def setWindowFlag()
        def setWindowFlags()
        def setWindowIcon()
        def setWindowIconText()
        def setWindowModality()
        def setWindowOpacity()
        def setWindowRole()
        def setWindowState()
        def size()
        def sizeIncrement()
        def sizePolicy()
        def stackUnder()
        def statusTip()
        def style()
        def styleSheet()

        def testAttribute()
        def toolTip()
        def toolTipDuration()
        def topLevelWidget()
        def underMouse()
        def ungrabGesture()
        def unsetCursor()
        def unsetLayoutDirection()
        def unsetLocale()
        def update()
        def updateGeometry()
        def updatesEnabled()
        def visibleRegion()
        def whatsThis()
        def winId()
        def window()
        def windowFilePath()
        def windowFlags()
        def windowHandle()
        def windowIcon()
        def windowIconText()
        def windowModality()
        def windowOpacity()
        def windowRole()
        def windowState()
        def windowTitle()
        def windowType()
        def x()
        def y()

Virtual methods

def actionEvent()

def changeEvent()

def closeEvent()

def contextMenuEvent()

def dragEnterEvent()

def dragLeaveEvent()

def dragMoveEvent()

def dropEvent()

def enterEvent()

def focusInEvent()

def focusNextPrevChild()

def focusOutEvent()

def hasHeightForWidth()

def heightForWidth()

def hideEvent()

def inputMethodEvent()

def inputMethodQuery()

def keyPressEvent()

def keyReleaseEvent()

def leaveEvent()

def minimumSizeHint()

def moveEvent()

def nativeEvent()

def paintEvent()

def resizeEvent()

def setVisible()

def showEvent()

def sizeHint()

Slots

def close()

def hide()

def lower()

def raise_()

def repaint()

def setDisabled()

def setEnabled()

def setFocus()

def setHidden()

def setStyleSheet()

def setWindowModified()

def setWindowTitle()

def show()

def showFullScreen()

def showMaximized()

def showMinimized()

def showNormal()

def update()

def updateMicroFocus()


Static functions

def find()

def keyboardGrabber()

def mouseGrabber()

def setTabOrder()


    def moveEvent( self, e ):

        if parent.isProcessingEvent( eUIEvent.eMove ) == False:
            return

    def resizeEvent( self, e ):

        if parent.isProcessingEvent( eUIEvent.eResize ) == False:
            return

            
            mouse buttons:
            
            
            Qt.NoButton

The button state does not refer to any button (see button() ).

Qt.AllButtons

This value corresponds to a mask of all possible mouse buttons. Use to set the ‘acceptedButtons’ property of a MouseArea to accept ALL mouse buttons.

Qt.LeftButton

The left button is pressed, or an event refers to the left button. (The left button may be the right button on left-handed mice.)

Qt.RightButton

The right button.

Qt.MiddleButton

The middle button.

Qt.BackButton

The ‘Back’ button. (Typically present on the ‘thumb’ side of a mouse with extra buttons. This is NOT the tilt wheel.)

Qt.XButton1

The ‘Back’ Button.

Qt.ExtraButton1

The ‘Back’ Button.

Qt.ForwardButton

The ‘Forward’ Button. (Typically present beside the ‘Back’ button, and also pressed by the thumb.)

Qt.XButton2

The ‘Forward Button.

Qt.ExtraButton2

The ‘Forward’ Button.

Qt.TaskButton

The ‘Task’ Button.

Qt.ExtraButton3

The ‘Task’ Button.


keyboard modifier keys can be found by calling the modifiers() function, inherited from QInputEvent .

The position() function gives the cursor position relative to the widget or item that receives the mouse event. If you move the widget as a result of the mouse event, use the global position returned by globalPosition() to avoid a shaking motion.

The setEnabled() function can be used to enable or disable mouse and keyboard events for a widget.

Qt.LeftButton
Qt.RightButton
Qt.MiddleButton

Qt.NoModifier - No modifier key is pressed.
Qt.ShiftModifier - A Shift key on the keyboard is pressed.
Qt.ControlModifier - A Ctrl key on the keyboard is pressed.
Qt.AltModifier - An Alt key on the keyboard is pressed.
Qt.MetaModifier - A Meta key on the keyboard is pressed.
Qt.KeypadModifier - A keypad button is pressed.


For example, to react to a Shift key + Left mouse button click:

MouseArea {
    onClicked: {
        if ((mouse.button == Qt.LeftButton) && (mouse.modifiers & Qt.ShiftModifier))
            doSomething();



QMouseEvent data:
            
    globalPos – PySide6.QtCore.QPointF
    modifiers – KeyboardModifiers
    device – PySide6.QtGui.QPointingDevice
    type – Type = MouseButtonPress , MouseButtonRelease , MouseButtonDblClick , or MouseMove 
    source – MouseEventSource
    arg__1 – PySide6.QtGui.QMouseEvent
    scenePos – PySide6.QtCore.QPointF
    button – MouseButton
    localPos – PySide6.QtCore.QPointF
    buttons – MouseButtons
    

    '''


