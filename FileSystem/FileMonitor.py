

# pylint: disable=no-name-in-module
from PySide6.QtCore import Slot, QObject, QFileSystemWatcher, QMutex, QMutexLocker

from AppUtils import GuardedDictionaryList, Logger
from FileSystem import FileMonitorUser


#
# File Monitor
#
# All objects/classes that use this file system monitor must implement functions:
#
#   def directoryChanged( self, path )
#   def fileChanged( self, path )
# 
# which are used for callbacks when change events take place
#         
class FileMonitor( QObject ):

    xref       = GuardedDictionaryList()
    mutex      = QMutex()        
    sysMonitor = QFileSystemWatcher()

        
    # init ourself
    def __init__(self):
    
        QObject.__init__(self)
        
        self.sysMonitor.directoryChanged.connect( self.dirChanged )
        self.sysMonitor.fileChanged.connect( self.fileChanged )
       
    
    # add a dir or file to monitor
    @staticmethod
    def addPath( path: str, owner: FileMonitorUser ) -> None:

        with QMutexLocker( FileMonitor.mutex ):
            
            FileMonitor.xref.addItem( path, owner )     # type: ignore
            FileMonitor.sysMonitor.addPath( path )
        
    
    # get list of watched directories
    @staticmethod
    def directories() -> list[str]:
        
        with QMutexLocker( FileMonitor.mutex ):
            return FileMonitor.sysMonitor.directories()
        
    
    # get list of watched files
    @staticmethod
    def files() -> list[str]:
        
        with QMutexLocker( FileMonitor.mutex ):
            return FileMonitor.sysMonitor.files()
        
    
    # see if a file or directory is being monitored
    @staticmethod
    def isMonitored(path: str) -> bool:
    
        with QMutexLocker( FileMonitor.mutex ):
            return FileMonitor.xref.hasKey( path )      # type: ignore
                
    
    # remove a dir or file from being monitored
    @staticmethod
    def removePath( path: str, owner: FileMonitorUser ) -> None:
        
        with QMutexLocker( FileMonitor.mutex ):
        
            FileMonitor.xref.removeItem( path, owner ) # type: ignore
            

    # callback if a directory changes
    @Slot(str)
    def dirChanged( self, path: str ) -> None:
    
        with QMutexLocker( self.mutex ):
            
            owners = self.xref.getItems( path )      # type: ignore
            for owner in owners:                     # type: ignore
                owner.directoryChanged( path )      

            else:
                assert( False )
                Logger.err( "FileSystemMonitor - Unknown Directory Change Event: {}".format( path ) )

    
    # callback if a file changes
    @Slot(str)
    def fileChanged( self, path: str ) -> None:

        with QMutexLocker( self.mutex ):
            
            owners = self.xref.getItems( path )     # type: ignore
            for owner in owners:                    # type: ignore
                owner.fileChanged( path )           # type: ignore



