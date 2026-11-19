
from AppDefs import DirDefs, Defs

from AppUtils import GuardedSet

from FileSystem import FileOperation, FileOpParent, EFileOpType


#
# Hyperlink Tracker - tracks all requested hyperlinks that have been explored over the entirety of the application
#
class HyperlinkTracker( FileOpParent ):

    OUTPUT_FILE = DirDefs.makePath( DirDefs.getCacheDir(), "VisitedHyperlinks.dat" )

    hyperlinks = GuardedSet()


    def __init__( self ):
        assert( self )
    

    @staticmethod
    def addHyperlink( hyperlink: str ) -> None:

        HyperlinkTracker.hyperlinks.addItem( hyperlink )


    @staticmethod
    def cleanseHyperlinks( hyperlinks: list[str] ) -> list[str]:

        retLinks = []               # type: ignore
        
        # cleanse of only new hyperlinks
        for link in hyperlinks:

            if link not in HyperlinkTracker.hyperlinks:        # type: ignore

                retLinks.append( link )                             # type: ignore
                HyperlinkTracker.hyperlinks.addItem( link )

        return retLinks                     # type: ignore



    # todo: AppStartup needs to call this function
    def readVisitedHyperlinks( self ) -> None:

        FileOperation.createReadLinesFileOp( self.OUTPUT_FILE, self, False )
        


    def writeHyperlinksFile( self ) -> None:

        FileOperation.createWriteLinesFileOp( self.OUTPUT_FILE, self.formatHyperlinks(), self, False )
        

    def formatHyperlinks( self ) -> list[str]:  # type: ignore

        fileLines = []
    
        setKeys = HyperlinkTracker.hyperlinks.getSet() # type: ignore

        line  = ""
        count = int(0)
        for val in setKeys:        # type: ignore

            line  += (val + Defs.COMDEL)      # type: ignore
            count += 1

            if count >= int(20):
                
                fileLines.append( line )        # type: ignore
                count = int(0)
                line  = ""

            

    def parseHyperlinks( self, fileOp: FileOperation ):

        for line in fileOp.data.lines:              # type: ignore
            vals = line.split( Defs.COMDEL )     # type: ignore
            for val in vals:                        # type: ignore
                HyperlinkTracker.hyperlinks.addItem( val )



    def fileOpComplete(self, fileOp: FileOperation ) -> None:
    
        if fileOp.handleError():
            return 

        if fileOp.type == EFileOpType.eRead:            # type: ignore
            self.parseHyperlinks( fileOp )  # type: ignore
            
        del fileOp
        