
from enum import Enum

from AppDefs import Defs
from AppServices import AppIndexer
from AppUtils import GuardedList
from AppDefs import SecurityStats



#
# Security - stock and etf tracking quick info
#
class Security:


    class EFields( Enum ):
    
        # skip 0 since position zero is used for file persistence formatting for class Stock
        eIndex          = 1
        eSymbol         = 2
        eCompany        = 3
        eIndustry       = 4
        eRating         = 5
        ePrice          = 6
        eMarketCap      = 7
        eRevenue        = 8
        eVolume         = 9
        eEarnings       = 10
        eNetIncome      = 11
        eShares         = 12
        eEPS            = 13
        ePE             = 14
        eForwardPE      = 15
        eDividend	    = 16
        eHiRange	    = 17
        eLoRange	    = 18
        eTarget         = 19
        eChange         = 20
        eDiff           = 21
        # these fields are only kept in our main all stocks listing for a stock or etf
        eNotes          = 22 # user notes area
        eRecords        = 23 # our special links to other records
        eNewsFeeds      = 24 # links to news feed items for this stock
        eRssFeeds       = 25 # links to rss feed items for this stock
        eMaxField       = 26 # must always be last
    


    # Strings for EField above
    FieldNames = [ 
        "",
        "Index",
        "Symbol",
        "Company",
        "Industry", 
        "Rating",
        "Price",
        "Market Cap",
        "Revenue", 
        "Volume",
        "Earnings",
        "Net Income",
        "Shares", 
        "EPS", 
        "PE",
        "Forward PE",
        "Dividend", 
        "High Range",  
        "Low Range",  
        "Target", 
        "Change", 
        "Difference" 
        ]



    def __init__( self ):

        self.uid       = AppIndexer.getCompanyUid()
        self.symbol    = ""
        self.name      = ""
        self.exchange  = ""
        self.stats     = GuardedList()
        

    def fromFileFmt(self, line: str ):
        
        pos             = line.find( Defs.BASDEL )
        if pos == -1:
            assert( False )
            return

        subline         = line[ 0 : pos ]
        values          = subline.split( Defs.COMDEL )
        
        self.uid        = values[0]
        self.symbol     = values[1]
        self.name       = values[2]
        self.exchange   = values[3] 

        return line[ pos : (len(line) - pos)]


    def toFileFmt(self) -> str:
        return (f"{self.uid}" + Defs.COMDEL + self.symbol + Defs.COMDEL + self.name + Defs.COMDEL + self.exchange + Defs.BASDEL) # type: ignore


    def getTableRow( self ) -> list[str]:
        return [ f"{self.uid}", self.symbol, self.name, self.stats.getItem(0).volume, self.stats.getItem(0).prevClose, self.stats.getItem(0).marketCap ]


    def parseJsonText( self, textLines: list[str] ):
        netchange = -1.0
        pctchange = -1.0
        country   = ""
        ipoyear   = ""
        industry  = ""
        sector    = ""
        url       = ""
        volume    = ""
        prevClose = 0
        marketCap = 0

        variables = [ self.symbol, self.name, prevClose, netchange, pctchange, volume, marketCap, country, ipoyear, industry, sector, url ]
    
        cnt = int(0)
        for line in textLines:
            pos             = (line.find( ":" ) + 1)
            variables[cnt]  = line[ pos : (len(line) - pos) ]
            cnt            += 1


        stat            = SecurityStats()
        stat.volume     = volume 
        stat.prevClose  = prevClose 
        stat.marketCap  = marketCap

        self.stats.addItem( stat )

