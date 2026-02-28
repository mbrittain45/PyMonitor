

from abc import ABC, abstractmethod

from enum import Enum

from FileSystem import FileData, FileSystemOps


#from typing import List, Deque, Dict, DefaultDict, OrderedDict, Union, Optional, 

#
# File Operation Result
#
class FileOpResult:

    def __init__( self ):

        self.done    = False
        self.failCnt = 0
        self.result  = True
        self.error   = ""

    def setFailed( self, err: str ):

        self.done    = True
        self.failCnt += 1
        self.result  = False
        self.error   = err

    def reset( self ):

        self.done    = False
        self.result  = True
        self.error   = ""

    def setPassed( self ):

        self.done    = True
        self.failCnt = 0
        self.result  = True
        self.error   = ""


#
# Abstract FileOperation Parent
# 
class AbstractFileOpParent(ABC):

    @abstractmethod
    def fileOpComplete(self, fileOp: FileOperation ) -> None:
        pass


#
# All task creators must derive from Task Parent for the callback
#
class FileOpParent( AbstractFileOpParent ):

    def __init__( self, name: str ):
        self.name = name

    # function must be implemented by derived class
    def fileOpComplete(self, fileOp: FileOperation ) -> None:

        assert( False ) 
        # todo: check for errors and clean up



#
# file operation types
#
class EFileOpType( Enum ):

    eUnknown    = 0x0000
    eRead       = 0x0001
    eWrite      = 0x0002
    eAppend     = 0x0004



#
# File Operation - a file operation which is given to AsyncFileTask to perform for users
#
class FileOperation:

    ETypeAsString   = [ "UNKNOWN", "READ", "WRITE", "APPEND" ]


    def __init__( self, filePath: str, parent: FileOpParent, binaryFile: bool ):
    
        self.filepath    = filePath
        self.type        = EFileOpType.eUnknown
        self.data        = FileData() 
        self.result      = FileOpResult()
        self.parent      = parent
        self.children    = None
        self.binary      = binaryFile
        

    def getOpAsStr( self ):

        return self.ETypeAsString[ self.type.value ]

        

        

        

        

    def isValid( self ) -> bool:
    
        if len( self.filepath ) <= 0:
            self.result.error = f"Invalid File Path: {self.filepath} - it can not be empty";
            return False

        if self.type == EFileOpType.eRead or self.type == EFileOpType.eAppend:
        
            if not FileSystemOps.doesFileExist( self.filepath ):
            
                if self.type == EFileOpType.eAppend:
                    self.type = EFileOpType.eWrite
            
            else:
            
                self.result.error = f"The File Path: {self.filepath} must exist for Reading and Appending file operations"
                return False


        type = int(self.type.value)
        if type > int(2):

            if not self.data.isValid():
                self.result.error = "The File Data must be valid for Writing and Appending File Operations";
                return False
        
        return True




    @staticmethod
    def createWriteFileOp( filePath: str, data: list[str], parent: FileOpParent, binary: bool ) -> FileOperation:

        fileOp      = FileOperation( filePath, parent, binary )
        fileOp.data = data
        fileOp.type = EFileOpType.eWrite
        return fileOp



    @staticmethod
    def createReadFileOp( path: str, parent: FileOpParent, binary: bool ) -> FileOperation:

        fileOp      = FileOperation( path, parent, binary )
        fileOp.type = EFileOpType.eRead
        return fileOp


