
'''
import os, io, shutil

from PySide6.QtCore import QLockFile

from AppUtils import CrcData, CrcCalculator, FileOps


#
# BinaryFile
# 
class BinaryFile:
    
    
    #
    # read an entire binary file. Return None if file doesn't exist, return 'crc-error' for crc errors and return the file data if the crc checks out
    #
    @staticmethod
    def read( fileName, readLines: bool ):

        if not FileOps.doesFileExist( fileName ):
            return None

        binData = ""
        lock  = QLockFile( fileName )
        with lock:
        
            size            = FileOps.getFileSize( fileName )
            if size > 0:

                file        = open( fileName, "rb", int(-1), encoding="utf-8" )
                if file.isreadable():

                    if readLines:
                        binData = file.readLines( size )
                    else:
                        binData = file.read( size )

                file.close()

        byteData = CrcCalculator.checkFileCRC( binData )
        if byteData != None:
            return binData.decode("utf-8")
        
        return "crc-error"
        

   
    #
    # write to a file 
    #
    @staticmethod
    def write( fileName, data, writeLines: bool ):
    
        binData  = data.encode('utf-8')
   
        crcCalc  = CrcCalculator( binData )
        crcCalc.calculateCRC()
        binData  = crcCalc.getByteDataWithCRC()

        lock            = QLockFile( fileName )
        with lock:
        
            file        = open( fileName, "wb", int(0), encoding="utf-8", errors='ignore' )
            if file.is_writable():

                if writeLines:
                    file.writeLines( binData )
                else:
                    file.write( binData )

            file.close()
        
   
    #
    # create an empty file to monitor
    #
    @staticmethod
    def createFile( filePath, lock: bool = True ):
        
        if FileOps.doesExist( filePath ) == False:
            f = open( filePath, "wb", int(-1),  encoding = "utf-8", errors='ignore' )
            f.close()
            return True

        return False


'''