



'''

import PySide6.QtWidgets import QWidget

from UserInterface import UIParent, eUIEvent


#
# UIMouseEvents - regisers for all mouse events then passes them
#                 up to the parent if they wanted the event. This
#                 way we are always watching for events in an easy
#                 to snap in base class but only pass up what the 
#                 parent wants
#

class UIMouseEvents( QWidget ):
    
    # init 
    def __init__( self, parent: UIParent ):
        super().__init__()
        self._parent = parent        
        self.mouseTracking( parent.isProcessingEvent( eUIEvent.eMouseTracking ) )
    
        
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



