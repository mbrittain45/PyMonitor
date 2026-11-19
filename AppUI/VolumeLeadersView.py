

'''


from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

#from PySide6.QtWidgets import QApplication, QMainWindow

from App import theApp
from AppDefs import Defs, EViewType 
from AppUI import SimpleTableWidget, WebView
from AppTasks.SystemTasks import VolumeLeadersTask



#
# News Feed URLs Table Widget
#
class VolumeLeadersView( SimpleTableWidget ):
    
   
    # init
    def __init__( self, uiLevel: int ):

        SimpleTableWidget.__init__( self, EViewType.eVolumeLeadersView, uiLevel )

        layout = QVBoxLayout()
        self.setLayout( layout )
        
        WebView( uiLevel + 1 )

        QWebEngineView.__init__( self )
        
        self.title = "Volume Leaders Table"
        
        self.setGeometry( Defs.getWindowGeometry( uiLevel ) )
        self.setContentsMargins( Defs.getWindowMargin() )
        self.createWindow( QWebEnginePage.WebWindowType.WebBrowserTab )
        self.load()

        self.task    = VolumeLeadersTask( self )               
 

    # update the table with values
    def updateView( self, htmlTable: str ):
        
        self.setUpdatesEnabled(False)
        self.clear()
                
        # Load the HTML content into the QWebEngineView
        self.setHtml( htmlTable )
        
        theApp.getMainWnd().setCentralWidget( self )
        
        self.setUpdatesEnabled(True)
    

    # double click short cut to view a story
    def doubleClickTable( self ):

        if self.hasSelection():
            selText  = self.selectedText()
            tableRow = self.__findTableRow__( selText )
            self.openNewWebTab( tableRow.url )



   #def findText()
   #def history()
   #def load()

def page()

def pageAction()

def print()

def printToPdf()

def selectedText()

def setContent()

def setHtml()

def setPage()

def setUrl()

def setZoomFactor()

def settings()

def title()

def triggerPageAction()

def url()

def zoomFactor()

Virtual methods
def createWindow()

Slots

def back()

def forward()

def reload()

def stop()



Signals

def loadFinished()

def loadProgress()

def loadStarted()

def pdfPrintingFinished()

def printFinished()

def printRequested()

def printRequestedByFrame()

def renderProcessTerminated()

def selectionChanged()

def titleChanged()

def urlChanged()

Static functions
def forPage()






#include <QWebEngineView>
#include <QMouseEvent>
#include <QEvent>
#include <QDebug>

class MouseEventHandler : public QObject
{
public:
    MouseEventHandler(QObject *parent = nullptr) : QObject(parent) {}

protected:
    bool eventFilter(QObject *obj, QEvent *event) override
    {
        if (event->type() == QEvent::MouseButtonPress ||
            event->type() == QEvent::MouseMove)
        {
            QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
            QPoint pos = mouseEvent->pos();
            qDebug() << "Mouse event at:" << pos;
        }
        return QObject::eventFilter(obj, event);
    }
};

// ... in your main widget or window
QWebEngineView *view = new QWebEngineView(this);
MouseEventHandler *handler = new MouseEventHandler(view);
view->focusProxy()->installEventFilter(handler);

// Enable mouse tracking to get mouseMoveEvent without a button press
view->setMouseTracking(true);








#include <QWebEngineView>
#include <QMouseEvent>
#include <QDebug>

class MyWebEngineView : public QWebEngineView
{
public:
    MyWebEngineView(QWidget *parent = nullptr) : QWebEngineView(parent)
    {
        // Enable mouse tracking to get mouseMoveEvent without a button press
        setMouseTracking(true);
    }

protected:
    void mousePressEvent(QMouseEvent *event) override
    {
        QPoint pos = event->pos(); // Position relative to the widget
        qDebug() << "Mouse pressed at:" << pos;
        QWebEngineView::mousePressEvent(event); // Call base class implementation
    }

    void mouseMoveEvent(QMouseEvent *event) override
    {
        QPoint pos = event->pos();
        qDebug() << "Mouse moved to:" << pos;
        QWebEngineView::mouseMoveEvent(event);
    }

    void mouseReleaseEvent(QMouseEvent *event) override
    {
        QPoint pos = event->pos();
        qDebug() << "Mouse released at:" << pos;
        QWebEngineView::mouseReleaseEvent(event);
    }
};



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.view.focusProxy().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj is self.ui.view.focusProxy() and event.type() == event.MouseButtonPress:
            print("Widget click")
        return super(MyWin, self).eventFilter(obj, event)

'''