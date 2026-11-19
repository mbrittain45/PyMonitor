
from datetime import datetime

from AppUtils import Epocher
from AppDefs  import Defs


#
# SecurityStats - shared statistics info used by both ETFs and Stocks
#
class SecurityStats:


    # init
    def __init__( self ):

        self.peRatio        = -1.0
        self.sharesOut      = -1
        self.dividend       = -1.0
        self.exdivDate      = Epocher.getDateTime()
        self.yearMin        = -1.0
        self.yearMax        = -1.0
        self.dayMin         = -1.0
        self.dayMax         = -1.0
        self.openPrice      = -1.0
        self.prevClose      = -1.0
        self.volume         = -1
        self.marketCap      = -1.0
        self.created        = datetime.now()

        # don't persist these values
        self.country       = ""
        self.ipoyear       = ""
        self.industry      = ""
        self.sector        = ""
        self.url           = ""
    

    # format to write to our file
    def toFileFmt( self ) -> str:

        return f"{self.peRatio},{self.sharesOut},{self.dividend},{self.yearMin},{self.yearMax},{self.dayMin},{self.dayMax},{self.openPrice},{self.prevClose},{self.volume},{self.exdivDate.isoformat()}{self.created.isoformat()}*" # type: ignore


    # unformat a read from our file
    def fromFileFmt(self, line: str ) -> str:
        
        pos = line.find( Defs.SHDDEL )
        if pos == -1:
            assert( False )
            return line

        subline         = line[ 0 : pos ]

        values          = subline.split( Defs.COMDEL )

        self.peRatio        = values[0]
        self.sharesOut      = values[1]
        self.dividend       = values[2]
        self.yearMin        = values[3]
        self.yearMax        = values[4]
        self.dayMin         = values[5]
        self.dayMax         = values[6]
        self.openPrice      = values[7]
        self.prevClose      = values[8]
        self.volume         = values[9]
        self.exdivDate      = datetime.fromisoformat( values[10] ) # type: ignore
        self.created        = datetime.fromisoformat( values[11] ) # type: ignore

        pos             += len(Defs.BASDEL)        

        return line[ pos : (len(line) - pos)]

