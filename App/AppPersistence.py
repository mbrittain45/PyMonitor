
'''


from App import Defs
from AppUtils import TextFile, FileOps


#
# App Persistence object - holds all values that need to be saved adn recovered
#
class AppPersistence:

    APP_PERSIST_FILE        = (Defs.APP_OUTPUT_DIR + Defs.DIR_SEP + "AppPersist" + Defs.DATA_EXT)

    # init ourself
    def __init__( self ):

        self._rssStoryFileIndex      = int(10)
        self._newsStoryFileIndex     = int(10)

        if FileOps.doesExist( self.APP_PERSIST_FILE ):

            lines = TextFile.read( self.APP_PERSIST_FILE, True )

            vals = lines[0].split( "," )
   
            assert( vals.count() == int(2))        
            self._rssStoryFileIndex  = vals[0]
            self._newsStoryFileIndex = vals[1]


    # get next rss story file index
    def getRssStoryFileIndex( self ):
    
        self._rssStoryFileIndex += 1
        self.persistValues()
        return ("rss" + self._rssStoryFileIndex)


    # get next news story file index
    def getNewsStoryFileIndex( self ):
        
        self._newsStoryFileIndex += 1
        self.persistValues()
        return ("nws" + self._newsStoryFileIndex)


    # persist our values to a file
    def persistValues(self):

        buffer = "{},{}".format( self._rssStoryFileIndex, self._newsStoryFileIndex )
        TextFile.queueWriteFile( self.APP_PERSIST_FILE, buffer, True, False )
        


'''