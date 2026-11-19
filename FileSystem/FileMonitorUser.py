


from abc import ABC, abstractmethod



#
# FileMonitorUser - all must override these functions to use the FileMonitor
# 
class FileMonitorUser( ABC ):

    @abstractmethod
    def directoryChanged( self, path: str ):
        pass


    @abstractmethod
    def fileChanged( self, path: str ):
        pass

