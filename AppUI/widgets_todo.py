


#from PySide6.QtWidgets import QListWidget, QListView, QPushButton, QRadioButton, QScrollArea, QScrollBar, QScroller, QSlider, QSpacerItem, QHBoxLayout
#from PySide6.QtWidgets import QGridLayout, QStackedLayout, QStackedWidget, QStatusBar

#class ListWidget( QListWidget ):
   
#    def __init__(self):
#        QListWidget.__init__(self)
#        QListWidget.setSortingEnabled( self, True )
        
        #addItem(label), addItem(item), addItems(labels), closePersistentEditor(item), count(), currentItem()
        #currentRow(), editItem(item), findItems(text, flags), indexFromItem(item), insertItem(row, item),
        #insertItems(row, labels),  isPersistentEditorOpen (item), isSortingEnabled (), item (row),  itemAt(p)
        #itemAt(x, y), itemFromIndex(index), itemWidget(item), items(data), openPersistentEditor (item),
        #removeItemWidget (item), row (item), selectedItems (), setCurrentItem (item), setCurrentItem (item, command),
        #setCurrentRow (row), setCurrentRow (row, command), setItemWidget (item, widget), setSortingEnabled (enable)
        #sortItems ([order=Qt.AscendingOrder]), takeItem (row), visualItemRect (item)

#class PushButton( QPushButton ):
   
#    def __init__(self, raised = True, default = False):
#        QPushButton.__init__(self)
#        if default:
#            QPushButton.default( True )
#        QPushButton.setFlat( raised )
        
    #menu (), setAutoDefault (arg__1), setDefault (arg__1), setFlat (arg__1), setMenu (menu), Slots: showMenu ()

#class RadioButton( QRadioButton ):
#    def __init__(self):
#        QRadioButton.__init__(self)

#class ScrollArea( QScrollArea ):
#    def __init__(self):
#        QScrollArea.__init__(self)
    #alignment (), ensureVisible (x, y[, xmargin=50[, ymargin=50]]), ensureWidgetVisible (childWidget[, xmargin=50[, ymargin=50]]),
    #setAlignment (arg__1), setWidget (widget), setWidgetResizable (resizable), takeWidget (), widget (), widgetResizable ()

#class ScrollBar( QScrollBar ):
 #   def __init__(self):
 #       QScrollBar.__init__(self)
        
#class Scroller( QScroller ):
#     def __init__(self):
#        QScroller.__init__(self)
    
    #finalPosition (), handleInput (input, position[, timestamp=0]), pixelPerMeter (), scrollerProperties (), setSnapPositionsX (positions)
    #setSnapPositionsX (first, interval), setSnapPositionsY (positions), setSnapPositionsY (first, interval), state (), stop (), target ()
    #velocity (), Slots: ensureVisible (rect, xmargin, ymargin), ensureVisible (rect, xmargin, ymargin, scrollTime), resendPrepareEvent ()
    #scrollTo (pos), scrollTo (pos, scrollTime), setScrollerProperties (prop) Signals: scrollerPropertiesChanged (arg__1), stateChanged (newstate)
    # Statics: activeScrollers (), grabGesture (target[, gestureType=QScroller.ScrollerGestureType.TouchGesture]), grabbedGesture (target)
    #hasScroller (target), scroller (target), scroller (target), ungrabGesture (target)

#class Slider( QSlider ):
#    def __init__(self):
 #       QSlider.__init__(self)
    
    #setTickInterval (ti), setTickPosition (position), tickInterval (), tickPosition (), initStyleOption (option)

# provides blank space in a layout
#class SpacerItem( QSpacerItem ):
#    def __init__(self):
#        QSpacerItem.__init__(self)
        
    #changeSize (w, h[, hData=QSizePolicy.Minimum[, vData=QSizePolicy.Minimum]]), sizePolicy ()

#class HorizontalBoxLayout( QHBoxLayout ):
#    def __init__(self):
#        QHBoxLayout.__init__(self)
       
    #addSpacing(), addStretch(), insertSpacing(), insertStretch()

#class GridLayout( QGridLayout ):
#    def __init__(self):
#        QGridLayout.__init__(self)

    #setRowMinimumHeight(), setRowStretch(), setColumnMinimumWidth(), setColumnStretch()

# provides a stack of widgets where only one widget is visible at a time
#class StackedLayout( QStackedLayout ):
#    def __init__(self):
#        QStackedLayout.__init__(self)
    
    #currentIndex (), currentWidget (), insertWidget (index, w), setStackingMode (stackingMode), stackingMode (), widget (arg__1)
    # Slots: setCurrentIndex (index), setCurrentWidget (w), signals: currentChanged (index), widgetRemoved (index)

#class StackedWidget( QStackedWidget ):
#    def __init__(self):
#        QStackedWidget.__init__(self)
    
    # addWidget (w), count (), currentIndex (), currentWidget (), indexOf (arg__1), insertWidget (index, w), removeWidget (w)
    # widget (arg__1), Slots: setCurrentIndex (index), setCurrentWidget (w) Signals: currentChanged (arg__1), widgetRemoved (index)

#class StatusBar( QStatusBar ):
#   def __init__(self):
#        QStatusBar.__init__(self)
    
    # addPermanentWidget (widget[, stretch=0]), addWidget (widget[, stretch=0]), currentMessage (), hideOrShow (), insertPermanentWidget (index, widget[, stretch=0])
    #insertWidget (index, widget[, stretch=0]), isSizeGripEnabled (), reformat (), removeWidget (widget), setSizeGripEnabled (arg__1), 
    # Slots: clearMessage (), showMessage (text[, timeout=0]), Signals: messageChanged (text)

# The QTextBrowser class provides a rich text browser with hypertext navigation. More…
# The QTextEdit class provides a widget that is used to edit and display both plain and rich text. More…

# The QTimeEdit class provides a widget for editing times based on the QDateTimeEdit widget. More…

# The QToolBar class provides a movable panel that contains a set of controls. More…

# The QUndoView class displays the contents of a QUndoStack. More…
# The QVBoxLayout class lines up widgets vertically. More…
# The QItemSelection class manages information about selected items in a model. More…
# The QIODevice class is the base interface class of all I/O devices in Qt. More…

# The QLineEdit widget is a one-line text editor. More…

# The QLayoutItem class provides an abstract item that a QLayout manipulates. More…

# The QLayout class is the base class of geometry managers. More…
# Inherited by: QStackedLayout, QGridLayout, QFormLayout, QBoxLayout, QVBoxLayout, QHBoxLayout


# The QCryptographicHash class provides a way to generate cryptographic hashes. More…
# The QDeadlineTimer class marks a deadline in the future. More…
# The QDir class provides access to directory structures and their contents. More…
# The QDirIterator class provides an iterator for directory entrylists. More…
# The QElapsedTimer class provides a fast way to calculate elapsed times. More…
# The QFileInfo class provides system-independent file information. More…
# The QItemSelection class manages information about selected items in a model. More…
# The QItemSelectionModel class keeps track of a view’s selected items. More…
# The QCursor class provides a mouse cursor with an arbitrary shape. More…
# The QDrag class provides support for MIME-based drag and drop data transfer. More…
# The QDropEvent class provides an event which is sent when a drag and drop action is completed. More…
# Inherited by: QDragMoveEvent, QDragEnterEvent
# The QIcon class provides scalable icons in different modes and states. More…
# The QImage class provides a hardware-independent image representation that allows direct access to the pixel data, and can be used as a paint device. More…
# The QImageReader class provides a format independent interface for reading images from files or other devices. More…
# The QKeyEvent class describes a key event. More…
# The QMouseEvent class contains parameters that describe a mouse event. More…
# QPageLayout - Describes the size, orientation and margins of a page. More…
# The QPageSize class describes the size and name of a defined page size. More…
# The QPicture class is a paint device that records and replays QPainter commands. More…
# The QRegion class specifies a clip region for a painter. More…
# The QSessionManager class provides access to the session manager. More…
# The QStaticText class enables optimized drawing of text when the text and its layout is updated rarely. More…
# The QSurface class is an abstraction of renderable surfaces in Qt. More…
# The QTextLayout class is used to lay out and render text. More…
# The QWindow class represents a window in the underlying windowing system. More…
# The QButtonGroup class provides a container to organize groups of button widgets. More…
# The QCalendarWidget class provides a monthly based calendar widget allowing the user to select a date. More…
# The QCheckBox widget provides a checkbox with a text label. More…
# The QColumnView class provides a model/view implementation of a column view. More…
# The QComboBox widget combines a button with a dropdown list. More…
# The QDockWidget class provides a widget that can be docked inside a QMainWindow or floated as a top-level window on the desktop. More…
# The QFileDialog class provides a dialog that allow users to select files or directories. More…


# The QBoxLayout class lines up child widgets horizontally or vertically. More…
#class BoxLayout( QBoxLayout ):

    # addLayout (layout[, stretch=0]), addSpacerItem (spacerItem), addSpacing (size), addStretch ([stretch=0]), addStrut (arg__1)
    # addWidget (arg__1[, stretch=0[, alignment=Qt.Alignment()]]), direction (), insertItem (index, arg__2), insertLayout (index, layout[, stretch=0])
    # insertSpacerItem (index, spacerItem), insertSpacing (index, size), insertStretch (index[, stretch=0]), insertWidget (index, widget[, stretch=0[, alignment=Qt.Alignment()]])
    # setDirection (arg__1), setStretch (index, stretch), setStretchFactor (l, stretch), setStretchFactor (w, stretch), stretch (index)
    
#class DateTimeCtrl( QDateTimeEdit ):

    #calendar (), calendarPopup (), calendarWidget (), clearMaximumDate (,clearMaximumDateTime (), clearMaximumTime (), clearMinimumDate ()
    # clearMinimumDateTime (), clearMinimumTime (), currentSection (), currentSectionIndex (), date (), dateTime (), displayFormat ()
    # displayedSections (), maximumDate (), maximumDateTime (), maximumTime (), minimumDate (), minimumDateTime (), minimumTime ()
    # sectionAt (index), sectionCount (), sectionText (section), setCalendar (calendar), setCalendarPopup (enable), setCalendarWidget (calendarWidget)
    # setCurrentSection (section), setCurrentSectionIndex (index), setDateRange (min, max), setDateTimeRange (min, max), setDisplayFormat (format)
    # setMaximumDate (max), setMaximumDateTime (dt), setMaximumTime (max), setMinimumDate (min), setMinimumDateTime (dt), setMinimumTime (min)
    # setSelectedSection (section), setTimeRange (min, max), setTimeSpec (spec), time (), timeSpec (), dateTimeFromText (text), textFromDateTime (dt)
    # Slots: setDate (date), setDateTime (dateTime), setTime (time), Signals: dateChanged (date), dateTimeChanged (dateTime), timeChanged (time)

# provides a group box frame with a title
#class GroupBox( QGroupBox ):
   
    # alignment (), isCheckable (), isChecked (), isFlat (), setAlignment (alignment), setCheckable (checkable)
    # setFlat (flat), setTitle (title), title (), initStyleOption (option), Slots: setChecked (checked)
    # Signals: clicked ([checked=false]), toggled (arg__1)


# provides a header row or header column for item views
# todo: class Header( QHeaderView ):


# provides a simple convenience dialog to get a single value from the user.
#class InputDlg( QInputDialog ):

    # cancelButtonText (), comboBoxItems (), doubleDecimals (), doubleMaximum (), doubleMinimum (), doubleStep (), doubleValue (), inputMode ()
    # intMaximum (), intMinimum (), intStep (), intValue (), isComboBoxEditable (), labelText (), okButtonText (), open (receiver, member)
    # setCancelButtonText (text), setComboBoxEditable (editable), setComboBoxItems (items), setDoubleDecimals (decimals), setDoubleMaximum (max)
    # setDoubleMinimum (min), setDoubleRange (min, max), setDoubleStep (step), setDoubleValue (value), setInputMode (mode), setIntMaximum (max)
    # setIntMinimum (min), setIntRange (min, max), setIntStep (step), setIntValue (value), setLabelText (text), setOkButtonText (text), setOption (option[, on=true])
    # setTextEchoMode (mode), setTextValue (text), testOption (option), textEchoMode (), textValue (), Signals: doubleValueChanged (value),
    # doubleValueSelected (value), intValueChanged (value), intValueSelected (value), textValueChanged (text), textValueSelected (text)
    # Statics: getDouble, getInt, getItem, getMultiLineText, getText
    

# provides a text or image display
#class Label( QLabel ):

    # alignment (), buddy (), hasScaledContents (), hasSelectedText (), indent (), margin (), movie (), openExternalLinks ()
    # picture (), pixmap (), selectedText (), selectionStart (), setAlignment (arg__1), setBuddy (arg__1), setIndent (arg__1)
    # setMargin (arg__1), setOpenExternalLinks (open), setScaledContents (arg__1), setSelection (arg__1, arg__2), setTextFormat (arg__1)
    # setTextInteractionFlags (flags), setWordWrap (on), text (), textFormat (), textInteractionFlags (), wordWrap (), Slots:
    #  clear (), setMovie (movie), setNum (arg__1), setNum (arg__1), setPicture (arg__1), setPixmap (arg__1), setText (arg__1)
    # Signals: linkActivated (link), linkHovered (link)

 
    





