

'''
from PySide6.QtCore import QLockFile

from AppUtils import FileOps, Log

#from AppTasks.TaskUtils import FunctionPtrTask


#
# Text File operations
#
class TextFile:


    @staticmethod
    def readlines( fileName: str ) -> list[str] : 

        data = []

        if not FileOps.doesFileExist( fileName ):
            return data
        
        lock = QLockFile( fileName )
        with lock:

            size = FileOps.getFileSize( fileName, False )
            if size > 0:
        
                file = open( fileName, "r", int(-1), encoding="utf-8" )
                if file.readable():
                    data = file.readLines( size )
                    file.close()
                   
        return data
    



       @staticmethod
    def readBlob( fileName: str ) ->  str :

        if not FileOps.doesFileExist( fileName ):
            return ""

        data = ""
        
        lock = QLockFile( fileName )
        with lock:

            size = FileOps.getFileSize( fileName, False )
            if size > 0:
        
                file = open( fileName, "r", int(-1), encoding="utf-8" )
                if file.readable():
                    data = file.read( size )
                    file.close()
                               
        return data

  
    @staticmethod
    def write( fileName, data: any, writeLines: bool ):
    
        lock = QLockFile( fileName )
        with lock:

            file = open( fileName, "w", int(0), encoding="utf-8", errors='ignore' )
            if file.writeable():
                if writeLines: 
                    file.writeLines( data )
                else:
                    file.write( data )
                file.close()
        

 
    @staticmethod
    def append( fileName, data: any, appendLines: bool ):
    
        lock = QLockFile( fileName )
        with lock:

            file = open( fileName, "a+", int(0), encoding="utf-8", errors='ignore' )
            if file.writeable():
                if appendLines: 
                    file.writeLines( data )
                else:
                    file.write( data )
                file.close()
        

    # do not call directly - perform a file write operation inside a task
    @staticmethod
    def performFileWrite( args ):

        if args != None:
            TextFile.write( args[0], args[1], args[2] )
        else:
            assert( False )
            Log.error( "TextFile.performFileWrite called with no args" )


    # do not call directly - perform a file append operation inside a task
    @staticmethod
    def performFileAppend( args ):

        if args != None:
            TextFile.append( args[0], args[1], args[2] )
        else:
            assert( False )
            Log.error( "TextFile.performFileAppend called with no args" )
            

    # queue a text file write operation
    @staticmethod
    def queueWriteFile( fileName, data: any, writeLines: bool, appendIfFileExists: bool = True ):

        # (fileName, data, writeLines) becomes args to the functions
        if FileOps.doesFileExist( fileName ) and appendIfFileExists:
            FunctionPtrTask( "TextFile.Append( {} )".format(fileName), None, TextFile.performFileAppend, (fileName, data, writeLines) ) 
        else:
            FunctionPtrTask( "TextFile.Write( {} )".format(fileName), None, TextFile.performFileWrite, (fileName, data, writeLines) )

  '''