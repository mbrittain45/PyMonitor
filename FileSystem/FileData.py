

from enum import Enum


class EFileDataType( Enum ):

    eUnknown   = 0x0000
    eStrings   = 0x0001
    eString    = 0x0002
    eBytes     = 0x0004
    



#
# FileData - holds the actual file data for reading, writing or appending
#
class FileData:
  
    def __init__( self, type: EFileDataType = EFileDataType.eUnknown ):

        self.type   = type
        self.lines  = list[str]
        self.blob   = ""
        self.bytes  = bytearray()


    def isValid( self ):

        if self.type == EFileDataType.eUnknown:     # type: ignore
            return False
        return True


    def setBytes( self, bytes: bytearray ):

        self.type   = EFileDataType.eBytes
        self.bytes  = bytes


    def setString( self, val: str ):

        self.type   = EFileDataType.eString 
        self.blob   = val


    def setStrings( self, vals: list[str] ):

        self.type   = EFileDataType.eStrings
        self.lines  = vals




