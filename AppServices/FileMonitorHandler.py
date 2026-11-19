

from FileSystem import FileMonitor, FileMonitorUser


#
# File Monitor Handler - handle the callbacks for files or directories being monitored via  the FileMonitor
#       that way the we'll get the callback and the other object can just check on us.
# 
class FileMonitorHandler( FileMonitorUser ):

    # init
    def __init__( self ):

        #FileMonitorUser.__init__(self)
        self.path      = ""
        self.changed   = False


    def addPath( self, path: str ):

        self.path = path
        FileMonitor.addPath( self.path, self )


    # check if the file or dir has changed    
    def hasChanged( self ):

        return self.changed

    
    # reset changed flag, call after has changed returns true
    def resetChanged( self ):

        self.changed = False


    # callback functon if a file changes
    def fileChanged( self, path: str ):
    
        if path == self.path:
            self.changed = True
        else:
            assert( False )


    # callback function if a directory changes
    def directoryChanged( self, path: str ):

        if path == self.path:
            self.changed = True
        else:
            assert( False )

