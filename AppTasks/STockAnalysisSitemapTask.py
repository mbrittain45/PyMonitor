

'''


from App import theApp

from AppDefs import Defs

from AppTasks import Task

from AppUtils import DirectoryOps, FileOps, TextFile, RequestUrl


#
# read StockAnalysis.com sitemap page looking for inteesting info
#
class StockAnalysisSitemapTask( Task ):

    OUTPUT_DIR      = Defs.addToCacheDir( "StockAnalysisSitemap" )
    OUTPUT_FILE     = Defs.makePath( OUTPUT_DIR, "StockAnalysisSitemap_{}.dat" )

    
    #
    # init ourself
    #
    def __init__( self ):

        DirectoryOps.createDir( self.OUTPUT_DIR )

        Task.__init__( self, "StockAnalysisSitemapTask", False, theApp.getTaskMgr() )

        self._url      = "https://stockanalysis.com/sitemap/"
        self._links    = []

        self.__startTask__()


    #
    # process the sitemap and all usefull data included
    #
    def processTask(self) -> bool:
 
        html = RequestUrl.get( self._url )
        if html != None:

            self.__parseHtml__( html )

        return True
'''