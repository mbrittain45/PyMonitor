
'''


from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

#from PySide6.QtWidgets import QApplication, QMainWindow

from App import theApp
from AppDefs import Defs, EViewType 
from AppUI import SimpleTableWidget
from AppTasks.SystemTasks import VolumeLeadersTask



#
# Web View - view derived from QWebEngineView
#
class WebView( QWebEngineView ):
    

    # init
    def __init__( self, uiLevel: int, title: str = "" ):

        QWebEngineView.__init__( self )

        self.title = title
        self.setGeometry( Defs.getWindowGeometry( uiLevel ) )
        self.setContentsMargins( Defs.getWindowMargin() )
        self.createWindow( QWebEnginePage.WebWindowType.WebBrowserTab )
        self.load()
   




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