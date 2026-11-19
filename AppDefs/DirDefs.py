


from FileSystem import FileSystem

#
# Directory Definitions
#
class DirDefs:
    
    # directory separator
    SEP                     = '/'

    # paths underneath us
    APP_DATA_PATH           = ('.' + SEP + 'Data' + SEP)
    APP_INPUT_PATH          = (APP_DATA_PATH + 'Input' + SEP)
    APP_OUTPUT_PATH         = (APP_DATA_PATH + 'Output' + SEP)
    APP_CACHE_PATH          = (APP_DATA_PATH + 'Cache' + SEP)
    
    @staticmethod
    def getInputDir() -> str:
        return DirDefs.APP_INPUT_PATH

    @staticmethod
    def getOutputDir() -> str:
        return DirDefs.APP_OUTPUT_PATH

    @staticmethod
    def getCacheDir() -> str:
        return DirDefs.APP_CACHE_PATH

    @staticmethod
    def createDirs() -> None:

        Directories = [ DirDefs.APP_DATA_PATH, DirDefs.APP_INPUT_PATH, DirDefs.APP_OUTPUT_PATH, DirDefs.APP_CACHE_PATH ]
        for directory in Directories:
            FileSystem.createDirs( directory )


    @staticmethod
    def addToDataDir( endDirName: str ) -> str:
 
       return (DirDefs.APP_DATA_PATH + endDirName + DirDefs.SEP)
    

    @staticmethod
    def addToInputDir( endDirName: str ) -> str:
        
        return (DirDefs.APP_INPUT_PATH + endDirName + DirDefs.SEP)
    

    @staticmethod
    def addToOutputDir( endDirName: str ) -> str:
        
        return (DirDefs.APP_OUTPUT_PATH + endDirName + DirDefs.SEP)
    
    
    @staticmethod
    def addToCacheDir( endDirName: str ) -> str:
        
        return (DirDefs.APP_CACHE_PATH + endDirName + DirDefs.SEP)
    

    @staticmethod
    def makePath( directory: str, endDirName: str ) -> str:
     
        return (directory + DirDefs.SEP + endDirName + DirDefs.SEP)




 
