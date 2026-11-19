

'''

from App import theApp

from AppDefs import Defs

from AppTasks import Task

from AppUtils import DirectoryOps, FileOps, TextFile


#
# Read the Top 50 Suggested Stocks by Analysts
#
class TopSuggestedStocksTask( Task ):

    OUTPUT_DIR     = Defs.addToCacheDir( "TopStocks" )
    OUTPUT_FILE    = Defs.makePath( OUTPUT_DIR, "TopStocks_{}.dat" )

    __url = "https://stockanalysis.com/analysts/top-stocks/"

    # init ourself
    def __init__( self ):

        DirectoryOps.createDir( self.OUTPUT_DIR )

        Task.__init__( self, "TopSuggestedStocksTask", False, theApp.getTaskMgr() )


        # todo: finish


'''