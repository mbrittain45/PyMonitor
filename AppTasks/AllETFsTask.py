

from AppBaseTask import RepeatingTask, TaskParent

from AppDefs import DirDefs

from AppServices import AppAbbrvApi
from FileSystem import FileSystem, FileOpParent
from AppUI import GenericPage, PageFunctionData


#
# All ETFs Task - we'll use a git repository to pull all stocks/company names from
#
class AllETFsTask( RepeatingTask, FileOpParent ):

    ALL_ETFS_DIR        = DirDefs.addToCacheDir( "ALL_ETFS" )
    REQUEST_ETFS_URL    = "https://etfdb.com/etfs/"
    ETF_RSP_FILE        = DirDefs.makePath( ALL_ETFS_DIR, "ETFsUrlRsp.txt" )
    ETF_INFO_FILE       = DirDefs.makePath( ALL_ETFS_DIR, "ETFs.txt" )
    ETFS_PAGE           = "ETFs PAGE"

    TABLE_HDRS          = [ "Symbol", "Price"  ] # todo:

    
    def __init__( self, parent: TaskParent ):
        
        RepeatingTask.__init__( self, "AllETFsTask", parent )
        
        FileSystem.createDir( self.ALL_ETFS_DIR )
           
        self.sleepTimeout   = int(2)
        self.fileOp         = None
                
        self.etfsPage       = GenericPage( PageFunctionData( AppAbbrvApi.getMainWidget(), self.ETFS_PAGE, 2, self.TABLE_HDRS ) )
        AppAbbrvApi.getMainWidget().addTab( self.etfsPage, self.ETF_PAGE )   # type: ignore

        self.__startTask__()


    # make the url request
    def makeRequest(self):

        assert( False )
        #if not RequestUrl.TimeSensitiveRequestUrl.requestAndSaveToFile( self.REQUEST_ETFS_URL, self.ETF_RSP_FILE, self ):
        #    Logger.err( f"Error requesting URL: {self.REQUEST_ETFS_URL}" )
            

'''
    # file operation callback
    def fileOpComplete( self, fileOp: FileOperation ):

        if fileOp.handleError():
            return

        self.fileOp = fileOp                


 
    # our processing task thread function
    def processTask(self) -> bool:

        if FileSystem.doesFileExist( self.ETF_RSP_FILE ):
            
 

        if self.fileOp == None:
            
            self.makeRequest()

        else:

            assert( False ) # todo
            # process the text in the fileOp
            #text = fileOp.data.lines[0]
                


        return ETaskResult.eSucceeded
                    

'''