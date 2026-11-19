

'''

from enum import Enum

from App import DateTimeFormat, GuardedDictionary, theApp, Defs, ViewObjectUpdate
from AppTasks import ETaskResult
from AppTasks.TaskUtils import RepeatingTask, BalanceSheet
from AppUtils import DirectoryOps, DTUtils, GuardedList, FileOps, TextFile, StockAnalysisUrl, RequestUrl, HtmlParser


#
# BalanceSheet Task - get balancesheet per stock, run once a quarter until finished w/ all stocks
#
class BalanceSheetTask( RepeatingTask ):


    def __init__( self ):

        RepeatingTask.__init__( self, "FinancialsTask", theApp.getTaskMgr() )

        self._lastReadStock = ""
        self._symbols       = GuardedList()
        self._sleepTime     = int(3)

        self.loadLists()
        self.readFile()
        
        self.__startTask__()
        

    def loadLists( self ):

        self.symbols.appendList( theApp.getNasdaqSymbols() )
        self.symbols.appendList( theApp.getNyseSymbols() )
        self.symbols.appendList( theApp.getAmexSymbols() )



    def processTask( self ) -> bool:

        if self._symbols.getCount() <= 0:
            self._repeatingTask = False
            return True
    
        index = int(0)
        for symbol in self._symbols:

            self._lastReadStock = symbol
            self.writeFile()

            url  = StockAnalysisUrl.getUrl( StockAnalysisUrl.EUrlType.eBalanceSheet, symbol )

            rsp  = RequestUrl.get( url )
            if rsp != None:
                balanceSheet = BalanceSheet( symbol )
                balanceSheet.processHtml( rsp )
            else:
                assert( False )
                return False

            self._symbols.popHead()
            
            index += 1
            if index > 15:
                return ETaskResult.eSucceeded

        return True


    # read our file and cleanse the symbols up to the last read
    def readFile(self):

        file = Defs.makePath( BalanceSheet.OUTPUT_DIR, "LastBalanceSheetSymbol" + Defs.DATA_EXT )
        if FileOps.doesExist( file ):
            self._lastReadStock = TextFile.read( file, True )
            for symbol in self._symbols:
                self._symbols.popHead()
                if symbol == self._lastReadStock:
                    return 
                

    def writeFile(self):
    
        file = Defs.makePath( BalanceSheet.OUTPUT_DIR, "LastBalanceSheetSymbol" + Defs.DATA_EXT )
        TextFile.queueWriteFile( file, self._lastReadStock, True, False )


'''