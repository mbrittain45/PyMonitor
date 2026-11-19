


from AppDefs import DirDefs
from AppUtils.Containers import GuardedDictionary
from FileSystem import FileOpParent, FileOperation, FileSystem


#
# AppIniFileReader - hold things like app look/feel customization
#
class AppIniFileReader( FileOpParent ):

    variables = GuardedDictionary()
    
    def __init__( self ):
        
        self.iniFilePath = DirDefs.addToInputDir( "stockApp.ini" )


    def readIniFile( self, filePath: str ) -> bool:

        if len( filePath ) > 0:
            if FileSystem.doesFileExist( filePath ):
                FileOperation.createReadLinesFileOp( filePath, self, False )
                return True
            
        if FileSystem.doesFileExist( self.iniFilePath ):
            FileOperation.createReadLinesFileOp( self.iniFilePath, self, False )
            return True

        return False
    

    def removeComment( self, line: str ) -> str:

        if line.find( ";" ) != -1:
    
            p1 = line.find( ";" )
            p2 = line.find( "=" )

            if p1 < p2:         # if comment is before = its invalid line
                return ""
            else:
                return line[ 0 : p1 ]

        elif line.find( "#" ) != -1:
    
            p1 = line.find( "#" )
            p2 = line.find( "=" )

            if p1 < p2:     # if comment is before = its invalid line
                return ""
            else:
                return line[ 0 : p1 ]
        
        else:
            assert( False )

        return ""


    def fileOpComplete(self, fileOp: FileOperation ) -> None:
    
        if fileOp.handleError():
            return
        
        lines: list[str] = fileOp.data.lines    # type: ignore
        for line in lines: 

            if line.find( ";" ) != -1 and line.find( "=" ) == -1:
                continue
            if line.find( "#" ) != -1 and line.find( "=" ) == -1:
                continue

            if line.find( ";" ) != -1 and line.find( "=" ) != -1:
                line = self.removeComment( line )
                if len( line ) <= 0:
                    continue

            if line.find( "#" ) != -1 and line.find( "=" ) != -1:
                line = self.removeComment( line )
                if len( line ) <= 0:
                    continue

            if line.find( "=" ) != -1:
                keyval = line.split( "=" )
                self.variables.addItem( keyval[0], keyval[1] )

        del fileOp


    @staticmethod
    def getKeys():

        return AppIniFileReader.variables.getKeys()


    @staticmethod
    def getValue( key: str ):

        return AppIniFileReader.variables.getItem( key )



''' todo:

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Accessing values
install_prefix = config['Installation']['prefix']
log_setting = config['Installation']['log_errors']

print(f"Installation Prefix: {install_prefix}")
print(f"Log Errors: {log_setting}") # Note: values are strings by default

'''