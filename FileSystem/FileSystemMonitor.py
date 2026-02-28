


'''
from PySide6.QtCore import Slot, QObject, QFileSystemWatcher, QMutex, QMutexLocker

from AppUtils import GuardedDictionaryList, Log


#
# File System Monitor
#
# All objects/classes that use this file system monitor must implement functions:
#
#   def directoryChanged( self, path )
#   def fileChanged( self, path )
# 
# which are used for callbacks when change events take place
#         
class FileSystemMonitor( QObject ):

    
    # init ourself
    def __init__(self):
    
        QObject.__init__(self)
        
        self._xref       = GuardedDictionaryList()
        self._mutex      = QMutex()        
        self._sysMonitor = QFileSystemWatcher( self )
        
        self._sysMonitor.directoryChanged.connect( self.dirChanged )
        self._sysMonitor.fileChanged.connect( self.fileChanged )
       
    
    # add a dir or file to monitor
    def addPath(self, path, owner ):

        with QMutexLocker( self._mutex ):
            
            self._xref.addItem( path, owner )
            self._sysMonitor.addPath( path )
        
    
    # get list of watched directories
    def directories( self ):
        
        with QMutexLocker( self._mutex ):
            return self._sysMonitor.directories()
        
    
    # get list of watched files
    def files( self ):
        
        with QMutexLocker( self._mutex ):
            return self._sysMonitor.files()
        
    
    # see if a file or directory is being monitored
    def isMonitored(self, path):
    
        with QMutexLocker( self._mutex ):
            
            path = self._xref.getItem( path )
            if path == None: 
                return False
            return True
    
    
    # remove a dir or file from being monitored
    def removePath( self, path ):
        
        with QMutexLocker( self._mutex ):
        
            removed = self._xref.popItem( path )
            if removed != None:
                self._sysMonitor.removePath( path )
    

    # callback if a directory changes
    @Slot(str)
    def dirChanged( self, path ):
    
        with QMutexLocker( self._mutex ):
            
            owner = self._xref.getItem( path )
            if owner != None: 
                owner.directoryChanged( path )
            else:
                assert( False )
                Log.error( "FileSystemMonitor - Unknown Directory Change Event: {}".format( path ) )

    
    # callback if a file changes
    @Slot(str)
    def fileChanged( self, path ):

        with QMutexLocker( self._mutex ):
            
            owner = self._xref.getItem( path )
            if owner != None: 
                owner.fileChanged( path )
            else:
                assert( False )
                Log.error( "FileSystemMonitor - Unknown File Change Event: {}".format( path ) )



'''