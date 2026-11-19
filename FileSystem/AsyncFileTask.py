

# pylint: disable=no-name-in-module
from PySide6.QtCore import QLockFile

from FileSystem import FileOperation, EFileOpType, EFileDataType, FileSystemOps

from AppBaseTask import Task, TaskParent


#
# Async File Task - is a singleton task that performs file operations asynchronously
#
class AsyncFileTask( Task ):

    FILE_LOCK_EXT   = ".lock";
    FILE_LOCK_TIME  = 5000;

    # init
    def __init__( self, fileOp: FileOperation, parent: TaskParent ):     # type: ignore

        Task.__init__( self, "AsyncFileTask", False, parent )
        self.fileOp = fileOp
        
    
    # process our work
    def processTask( self ) -> bool:

        match self.fileOp.type:             # type: ignore

            case EFileOpType.eRead:
                self.readFile()

            case EFileOpType.eWrite:
                self.writeFile()

            case EFileOpType.eAppend:
                self.appendFile()

            case EFileOpType.eUnknown:
                return False

        return True


    def readFile( self ):

        lock = QLockFile( self.fileOp.filepath + self.FILE_LOCK_EXT )
        lock.setStaleLockTime( self.FILE_LOCK_TIME );

        mode = "r"
        if self.fileOp.binary == True:
            mode += "b"

        file = open( self.fileOp.filepath, mode, int(-1), encoding="utf-8" )

        if file.readable():

            size = FileSystemOps.getFileSize( self.fileOp.filepath, False ) # type: ignore
            if size <= 0:
                self.fileOp.result.setFailed( f"the File: {self.fileOp.filepath} is an empty file" )
                return
        
            if self.fileOp.data.type == EFileDataType.eStrings:
                self.fileOp.data.setStrings( file.readlines() )
            else:
                if self.fileOp.data.type == EFileDataType.eBytes:
                    self.fileOp.data.setBytes( file.read() )
                else:
                    self.fileOp.data.setString( file.read() )
        
            file.close()

        
        self.fileOp.result.setPassed()
        if self.fileOp.parent:
            self.fileOp.parent.fileOpComplete( self.fileOp )
        else:
            assert( False )


   
    def writeFile( self ):
    
        lock = QLockFile( self.fileOp.filepath + self.FILE_LOCK_EXT )
        lock.setStaleLockTime( self.FILE_LOCK_TIME );

        mode = "w"
        if self.fileOp.binary == True:
            mode += "b"

        file = open( self.fileOp.filepath, mode, int(-1), encoding="utf-8" )
        if file.writable():

            if self.fileOp.data.type == EFileDataType.eStrings:
                file.writelines( self.fileOp.data.lines )           # type: ignore
            else:
                if self.fileOp.data.type == EFileDataType.eBytes:
                    file.write( self.fileOp.data.bytes )
                else:
                    file.write( self.fileOp.data.blob )
       
            file.close()

        self.fileOp.result.setPassed()
        if self.fileOp.parent != None:  # type: ignore
            self.fileOp.parent.fileOpComplete( self.fileOp )



    def appendFile( self ):
    
        lock = QLockFile( self.fileOp.filepath + self.FILE_LOCK_EXT )
        lock.setStaleLockTime( self.FILE_LOCK_TIME );

        mode = "a+"
        if self.fileOp.binary == True:
            mode += "b"

        file = open( self.fileOp.filepath, mode, int(-1), encoding="utf-8" )
        if file.writable():

            if self.fileOp.data.type == EFileDataType.eStrings:
                file.writelines( self.fileOp.data.lines )           # type: ignore
            else:
                if self.fileOp.data.type == EFileDataType.eBytes:
                    file.write( self.fileOp.data.bytes )
                else:
                    file.write( self.fileOp.data.blob )
       
            file.close()

        self.fileOp.result.setPassed()
        if self.fileOp.parent != None:  # type: ignore
            self.fileOp.parent.fileOpComplete( self.fileOp )



'''

    todo:
    // if binary file check the crc
    if ( binary )
    {
        CrcData readCrcData();
        vector<uint8_t> byteData;
        for ( int i = 0; i < 3; ++i )
        {
            char c = static_cast<char>( data[ i ] );
            byteData.emplace_back( c );
        }
        readCrcData.parse( data );


        vector<uint8_t> byteData = convertToBytes( data );

        CRCCalculate crcCalc;
        if ( ! crcCalc.parseAndCheckCrc( byteData ) )
        {
            CrcData crcData;
            crcData.
            Logger::getInstance()->error( format("The CRC for File: {} was not correct. Was: {} should be {}", fileName, crcCalc.mCrcValue,  )
            data.clear();
        }

vector<uint8_t> AsyncFileTask::ComputeCrcAndBuffer( const vector<string>& data )
{
    vector<uint8_t> byteData;
    for ( int i = 0; i < data.size(); ++i )
    {
        string str = data.at( i );
        for ( int j = 0; j < str.length(); ++j )
            byteData.emplace_back( str[j] );
    }

    CrcCalc crcCalc;
}


'''
