


'''


from PySide6.QtCore import QFile, QIODevice, QDataStream

from App import Defs

# todo:

#
# Persistor - for persisting object data
#
class AppPersistor:
    
    #
    # init ourself
    #
    def __init__( self, filePath: str, writing: bool ):
        
        self.filePath = filePath
        self.writing  = writing
        
        file = QFile( self.filePath )
        if writing:
            file.open(QIODevice.WriteOnly)
        else:
            file.open(QIODevice.ReadOnly) 

        self.qstream = QDataStream( file )
        

    #
    # write value out
    #
    def __writeValue__( self, datatype: Defs.EDataType, value ):
        
        self.qstream.writeInt32( int(datatype) )

        match datatype:
        
            case Defs.EDataType.eBoolDT:
                self.qstream.writeBool( value )
            
            case Defs.EDataType.eIntDT:
                self.qstream.writeInt32( value )
            
            case Defs.EDataType.eFloatDT:
                self.qstream.writeFloat( value )
            
            case Defs.EDataType.eStringDT:
                self.qstream.writeString( value )
            
            case Defs.EDataType.eRawDataDT:
                length, rawdata = value
                length = len( rawdata )
                self.qstream.writeInt32( length )
                self.qstream.writeRawData( rawdata )                
            
            case Defs.EDataType.eBytesDT:
                length, cbytes = value
                length = len( cbytes )
                self.qstream.writeInt32( length )
                self.qstream.writeBytes( cbytes )
                
    
    # write values out
    def writeValues( self, datatypes: list[Defs.EDataType], valuesList ):
        
        self.qstream.startTransaction()
        
        index = int(0)
        dtLen = len( datatypes  )
        while index < dtLen:
            self.__writeValue__( datatypes[ index ], valuesList[ index ] )
            index += 1
            

    #
    # read values in
    #
    def readValues( self, datatypes: list[Defs.EDataType] ):
        
        retVals = []
        
        self.qstream.startTransaction()
        
        index = int(0)
        dtLen = len( datatypes  )
        while index < dtLen:
            retVals.append( self.__readValue__( self.qstream.readInt32() ) )
            index += 1
        
        return retVals


    #
    # read a value in
    #
    def __readValue__( self, datatype: Defs.EDataType ):
        
        match datatype:
        
            case Defs.EDataType.eBoolDT:
                return self.qstream.readBool()
                            
            case Defs.EDataType.eIntDT:
                return self.qstream.readInt32()
             
            case Defs.EDataType.eFloatDT:
                return self.qstream.readFloat()
                           
            case Defs.EDataType.eStringDT:
                return self.qstream.readString()
                            
            case Defs.EDataType.eRawDataDT:
                
                length  = self.qstream.readInt32()
                rawData = self.qstream.readRawData( length )                
                return (length, rawData)
            
            case Defs.EDataType.eBytesDT:

                length = self.qstream.readUInt32()
                cbytes = self.qstream.readBytes( length )
                return (length, cbytes)
                


'''