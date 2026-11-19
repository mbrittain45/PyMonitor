
import sys 

# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QGuiApplication, QFont, QSessionManager


from enum import Enum 

from App import AppIniFileReader, StockAppWindow

from AppDefs import DirDefs
from AppBaseTask import TaskManager, TaskParent, Task
from AppUtils import Logger, GuardedList
from AppServices import HyperlinkTracker


class EFontType( Enum ):

    eStockFont = int(0)
    eMenuFont  = int(1)
    eBigFont   = int(2)
    eSpecFont  = int(3)
    eMaxFont   = int(4)


#
# the Application
#
class StockApp( QGuiApplication, TaskParent ):

    # clean up our complete tasks
    def taskComplete( self, task: Task ):
    
        print( f"Task {task.taskName}::{task.taskId} - is complete" )
        del task



    # init the application
    def __init__(self):

        # todo:

        # command line args are processed here.
        # 1. We allow a special ini file name
        self.iniFilePath = ""
        if len( sys.argv ) > 1:
            self.iniFilePath = sys.argv[1]

        self.iniFileReader = AppIniFileReader()
        if not self.iniFileReader.readIniFile( self.iniFilePath ):
            err = f"Unable to find and read INI File: {self.iniFilePath} or {self.iniFileReader.iniFilePath}"
            print( err )
            Logger.err( err )
        
        # 2.
        #if len( sys.argv ) > 2:
        #    self.iniFilePath = sys.argv[2]

        DirDefs.createDirs()

        QGuiApplication.__init__(self)

        self.setApplicationDisplayName( "Stock Up App" )
        self.setQuitOnLastWindowClosed( True )
        self.setApplicationName( "Stock App" )
        self.setQuitLockEnabled( True )

        self.initialized        = False
        self.taskManager        = TaskManager()
        self.appPaused          = False

        self.fonts              = GuardedList()

        self.fonts.addItem( QFont("Times", 10) )    # stock name/symbol font
        self.fonts.addItem( QFont("Arial", 12) )    # menus font
        self.fonts.addItem( QFont("Verdana", 15) )  # big font
        self.fonts.addItem( QFont("Helvetica", 13) )# special font
        
        self.applicationStateChanged.connect( self.appStateChangedSlot )
        self.commitDataRequest.connect( self.appCommitDataSlot )
        # todo:
        #self.lastWindowClosed.connect( self.appLastWndClosedSlot )
        #self.primaryScreenChanged.connect( self.appScreenChangedSlot )
        #self.saveStateRequest.connect( self.appSaveStateSlot )
   
        Logger.einfo( "Application PID: {}".format( self.applicationPid() ) )
        Logger.einfo( "Application State: {}".format( self.applicationState() ) )
        Logger.einfo( "Application Directory: {}".format( self.applicationDirPath() ) )
        Logger.einfo( "Application Session ID: {}".format( self.sessionId() ) )
        Logger.einfo( "Application Session Key: {}".format( self.sessionKey() ) )
       
        # finally create our main window
        self.mainWindow: StockAppWindow = StockAppWindow( self.primaryScreen().size() )
        self.mainWindow.show()

        self.hyperlinkTracker = HyperlinkTracker()
        self.hyperlinkTracker.readVisitedHyperlinks()



    def getMainWindow( self ) -> StockAppWindow:
        return self.mainWindow


    def setUnableToInitialize( self ) -> None:
        assert( False )
        # todo: tell the user


    def isInitialized( self ) -> bool:
        return self.initialized

    
    def setInitialized( self, flag: bool ) -> None:
        self.initialized = flag 


    def getFont( self, fontType: EFontType) -> QFont:
        return self.fonts.getItem( int( fontType ) )    # type: ignore


    def getTaskMgr(self) -> TaskManager:
        return self.taskManager



    #
    # Slots
    #
    @Slot()
    def appStateChangedSlot( self, state: Qt.ApplicationState ):
        assert( state )
        assert( False )

    @Slot()
    def appCommitDataSlot( self, mgr: QSessionManager ):
        assert( mgr )
        assert( False )
       

   # @Slot()
   # def appLastWndClosedSlot( ):
        # todo: Logger.writeLog( "Exiting Application" )
   #     exit( 0 );

        
''' todo:

    @Slot()
    def appScreenChangedSlot( screen : QScreen ):
        assert( screen )
        assert( False )

    @Slot()
    def appSaveStateSlot( mgr: QSessionManager ):
        assert( mgr )
        assert( False )


#    def getReporter(self):
#        return self._reporter 
 

    def pauseApplication(self, pause: bool ) -> None:
        
        self.appPaused = pause
        if not self.appPaused:
            self.taskManager.startWaitingTasks()
        

    def isApplicationPaused( self ) -> bool:
        return self.appPaused
        
        
    # get the main window
    def getWnd(self):
        return self._theWnd


    def getStatusBar( self ):
        self.mainWindow.getStatusBar()

        # create our other dictionaries
        FunctionPtrTask( "CreateOtherDictionaries", self, self.createDictionaries )

        # write out our companies file
        FunctionPtrTask( "WriteCompaniesFile", self, self.writeCompaniesFile )

        # write out our statistics companies file
        FunctionPtrTask( "WriteDailyStatistics", self, self.writeDailyStatistics )
    
'''
    

 
 






