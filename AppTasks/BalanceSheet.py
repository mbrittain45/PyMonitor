

'''

from enum import Enum

from App import DateTimeFormat, GuardedDictionary, theApp, Defs, ViewObjectUpdate
from AppUtils import DirectoryOps, DTUtils, FileOps, TextFile, FileDelimiterTimestmap, HtmlParser


#
# BalanceSheet - balancesheet per stock, run once a quarter until finished w/ all stocks
#
class BalanceSheet():

    OUTPUT_DIR     = Defs.addToCacheDir( "BalanceSheet" )
    STOCK_FILE     = Defs.makePath( OUTPUT_DIR, "{}_BalanceSheet" + Defs.DATA_EXT )
    
    Keywords = [ 
        "Cash & Equivalents", 
        "Short-Term Investments", 
        "Accounts Receivable", 
        "Property, Plant & Equipment",
        "Goodwill", 
        "Investments in Debt & Equity Securities", 
        "Long-Term Deferred Tax Assets",
        "Total Assets", 
        "Accounts Payable", 
        "Accrued Expenses", 
        "Long-Term Deferred Tax Liabilities", 
        "Total Liabilities", 
        "Common Stock", 
        "Retained Earnings",
        "Comprehensive Income & Other", 
        "Total Common Equity", 
        "Shareholders' Equity", 
        "Total Liabilities & Equity",
        "Total Debt", 
        "Net Cash Per Share", 
        "Total Common Shares Outstanding",
        "Working Capital", 
        "Book Value Per Share", 
        "Tangible Book Value", 
        "Tangible Book Value Per Share"
    ]


    def __init__( self, symbol ):
        
        DirectoryOps.createDir( self.OUTPUT_DIR )
        
        self._symbol    = symbol  
        self._htmlTable = ""
        self._values    = []
        for key in self.Keywords:
            self._values.append( float(0.0) )


    def processHtml( self, rsp ):

        self._htmlTable = HtmlParser.parseMainTableBody( rsp )
        
        for keyword in self.Keywords:

            rowVals = HtmlParser.getTableRow( keyword, self._htmlTable )
            self._values.append( float( rowVals[0] ) )

        theApp.getTaskMgr().updateView( ViewObjectUpdate( Defs.EViewType.eBalanceSheet, self ) )
        self.writeFile()


    def readFile( self ):
        
        data = TextFile.read( self.STOCK_FILE.format( self._symbol ), False )
        if len( data ) > 0:

            timedValues  = FileDelimiterTimestmap.parse( data )
            valuesBlob   = timedValues.getItem( timedValues.getKeys()[0] )
            self._values = valuesBlob.split( Defs.COM_DEL )

        else:
            assert( False )


    def readAllQuartersFromFile( self, symbol ) -> GuardedDictionary:
        
        data = TextFile.read( self.STOCK_FILE.format( symbol ), False )
        if len( data ) > 0:
            return FileDelimiterTimestmap.parse( data )
        else:
            assert( False )


    # keep newest values at the head of the file
    def writeFile( self, symbol ):

        buf = FileDelimiterTimestmap.get()
        for val in self._values:
            buf += (val + Defs.COM_DEL)
        buf += TextFile.read( self.STOCK_FILE.format( symbol ), False )

        TextFile.queueWriteFile( self.STOCK_FILE.format( symbol ), buf, False, False )
    


'''