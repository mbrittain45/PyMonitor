

import random

from AppUtils import Logger

from fastcrc import crc64

from enum import IntEnum

#from crc import Calculator, Crc64


#
# CRC algorithm types
#
class ECrcAlgorithm( IntEnum ):

    eCRC_ECMA182   = int(1)
    eCRC_GO_ISO    = int(2)
    eCRC_WE        = int(3)
    eCRC_XZ        = int(4)



#
# CrcData - holds needed crc data for checking file validity
#
class CrcData:

    CRC_DATA_LEN = int(16)

    # init ourself
    def __init__( self, byteData: bytearray, crcAlgo: ECrcAlgorithm = ECrcAlgorithm.eCRC_ECMA182 ):

        self.byteData     = byteData
        self.crcValue     = int(-0)
        self.crcAlgo      = crcAlgo


    # compare two objects
    def __eq__( self, other: CrcData ) -> bool:     # type: ignore

        if self.crcAlgo != other.crcAlgo:
            return False
        if self.crcValue != other.crcValue:
            return False 
    
        return True



    # buffer our crc byte data
    def buffer( self ) -> bytearray:

        crcByteData     = bytearray()
        
        crcByteData.extend( self.crcAlgo.to_bytes( 8, byteorder='big' ) )
        crcByteData.extend( self.crcValue.to_bytes( 8, byteorder='big' ) )
        
        assert( len( crcByteData ) == self.CRC_DATA_LEN )
   
        crcByteData.extend( self.byteData )

        return crcByteData



    # parse our crc byte data
    def parse( self ):

        crcAlgoBytes = bytearray()
        crcValBytes  = bytearray()

        index = int(0)
        while index < 8:    # 0-7
            crcAlgoBytes.append( self.byteData[ index ] )
            index += 1

        while index < 16:  # 8-15
            crcValBytes.append( self.byteData[ index ] )
            index += 1

        self.crcAlgo  = int.from_bytes( crcAlgoBytes, byteorder='big' )
        self.crcValue = int.from_bytes( crcValBytes, byteorder='big' )
   
        if self.crcAlgo < ECrcAlgorithm.eCRC_ECMA182 or self.crcAlgo > ECrcAlgorithm.eCRC_XZ:
            return False
        
        return True



    
#
# CRC Calculator - calculates a crc64 over a file w/ a certain crc64 algorithm
#
class CrcCalculator():
  
    # init ourself
    def __init__( self, byteData: bytearray, crcAlgo: ECrcAlgorithm = ECrcAlgorithm.eCRC_ECMA182 ):

        self.crcData = CrcData( byteData, crcAlgo )
        

    # get our file crc object
    def getByteDataWithCRC( self ):
        return self.crcData.buffer()

        
    # get the file crc data
    def getCrcData( self ):
        return self.crcData
    

    # get random range based value
    @staticmethod
    def __getRandomRangedValue__( lowRange: int, hiRange: int ) -> int:
        
        return random.randrange( lowRange, hiRange, 0 )



    # cacluate the crc
    def calculateCRC( self ):

        if self.crcData.crcAlgo == int(0):
            self.crcData.crcAlgo = self.__getRandomRangedValue__( 1, 4 )

        match self.crcData.crcAlgo:

            case ECrcAlgorithm.eCRC_ECMA182:
                self.crcData.crcValue = crc64.ecma_182( bytes( self.crcData.byteData ) )
            case ECrcAlgorithm.eCRC_GO_ISO:
                self.crcData.crcValue = crc64.go_iso( bytes( self.crcData.byteData ) )
            case ECrcAlgorithm.eCRC_WE:
                self.crcData.crcValue = crc64.we( bytes( self.crcData.byteData ) )
            case ECrcAlgorithm.eCRC_XZ:
                self.crcData.crcValue = crc64.xz( bytes( self.crcData.byteData ) )
            case _:
                Logger.error( f"Invalid CRC Calculation Type Selected: {self.crcData.crcAlgo}" ) # type: ignore
                return False

        return True 



    # check a files crc
    @staticmethod
    def checkFileCRC( binaryData: bytearray ) :

        # parse exiting file crc data
        fileCrc = CrcData( binaryData );
        fileCrc.parse();
        
        # parse the existing crc data
        recalcCrc = CrcData( binaryData )
        recalcCrc.parse()

        # calculate the crc
        recalcCrcCalc = CrcCalculator( recalcCrc.byteData, recalcCrc.crcAlgo )  # type: ignore
        if recalcCrcCalc.calculateCRC():
                 
            # check the crcs against each other
            crcData = recalcCrcCalc.getCrcData()
            if fileCrc.crcValue == crcData.crcAlgo and crcData.crcValue == fileCrc.crcValue:
                return fileCrc.byteData

        return None



