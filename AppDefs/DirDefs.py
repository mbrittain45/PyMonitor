


from FileSystem import FileSystemOps

#
# Directory Definitions
#
class DirDefs:
    
    # directory separator
    DIR_SEP                 = '/'

    # paths underneath us
    APP_DATA_PATH           = ("." + DIR_SEP + 'Data' + DIR_SEP)
    APP_INPUT_PATH          = (APP_DATA_PATH + 'Input' + DIR_SEP)
    APP_OUTPUT_PATH         = (APP_DATA_PATH + 'Output' + DIR_SEP)
    APP_CACHE_PATH          = (APP_DATA_PATH + 'Cache' + DIR_SEP)
    
    # file delimiters
    COM_DEL                 = ","
    END_DEL                 = "\n"
    BAS_DEL                 = ";"
    DER_DEL                 = "-"
    TOP_DEL                 = "="
    CMT_DEL                 = "#"
    
    # others
    DATA_EXT                = ".dat"
    SENTENCE_ENDINGS        = [ ".", "?", "!" ]
   
    @staticmethod
    def getInputDir():
        return DirDefs.APP_INPUT_PATH

    @staticmethod
    def getOutputDir():
        return DirDefs.APP_OUTPUT_PATH

    @staticmethod
    def getCacheDir():
        return DirDefs.APP_CACHE_PATH

    @staticmethod
    def createDirs():

        Directories = [ DirDefs.APP_DATA_PATH, DirDefs.APP_INPUT_PATH, DirDefs.APP_OUTPUT_PATH, DirDefs.APP_CACHE_PATH ]

        for directory in Directories:

            FileSystemOps.createDirs( directory )


    @staticmethod
    def addToDataDir( endDirName: str = '' ):
 
       return (DirDefs.APP_DATA_PATH + endDirName)
    

    @staticmethod
    def addToInputDir( endDirName: str = '' ):
        
        return (DirDefs.APP_INPUT_PATH + endDirName)
    

    @staticmethod
    def addToOutputDir( endDirName: str = '' ):
        
        return (DirDefs.APP_OUTPUT_PATH + endDirName)
    
    
    @staticmethod
    def addToCacheDir( endDirName: str = '' ):
        
        return (DirDefs.APP_CACHE_PATH + endDirName)
    

    @staticmethod
    def makePath( directory: str, endDirName: str = "" ):
     
        return (directory + DirDefs.DIR_SEP + endDirName)




 
