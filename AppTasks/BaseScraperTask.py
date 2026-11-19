

from AppTasks import RepeatingTask, TaskParent
from FileSystem import FileOperation, FileSystem, FileOpParent, EFileOpType
from AppServices import FileMonitorHandler, AppAbbrvApi
from AppUtils import GuardedQueue
from AppUI import PageFunctionData, GenericPage
from AppDefs import ViewData, ViewUser


#
# Base Scraper Task - we search for news about companies
#
class BaseScraperTask( RepeatingTask, FileOpParent, ViewUser ):

    
    # init
    def __init__( self, taskname: str, parent: TaskParent, fieldNames: list[str], inputFile: str ):
        
        RepeatingTask.__init__( self, taskname, parent )

        self.sleepTimeout       = int(2)
        self.loading            = False
        self.urls               = GuardedQueue()
        self.hyperlinks         = GuardedQueue()
        self.fileMonitor        = FileMonitorHandler()
        self.inputFile          = inputFile

        assert( len( self.inputFile ) > 0 )

        # create our page functional data
        pageFuncData            = PageFunctionData( AppAbbrvApi.getMainWidget(), taskname, 2, fieldNames )

        pageFuncData.rowDeletable       = True
        pageFuncData.rowHideable        = True
        pageFuncData.columnDeletable    = True
        pageFuncData.columnHideable     = True
        pageFuncData.columnReordering   = True
        
        # create our generic display page
        self.scraperPage        = GenericPage( pageFuncData ) 

        # add our page tab to the main widget
        AppAbbrvApi.getMainWidget().addTab( self.scraperPage, taskname )   # type: ignore

        # create our update view data
        self.pageData          = ViewData( taskname, self )

        self.readInputFile()


    # read our input file if we have one and monitor the file
    def readInputFile( self ) -> None:

        if FileSystem.doesFileExist( self.inputFile ):
            FileOperation.createReadLinesFileOp( self.inputFile, self, False )
            if len( self.fileMonitor.path ) <= 0:
                self.fileMonitor.addPath( self.inputFile ) 
                

    # parse our urls 
    def parseUrls( self, fileOp: FileOperation ) -> None:

        self.loading = True

        index = 0        
        for line in fileOp.data.lines:          # type: ignore
            self.urls.addTail( line )
            self.pageData.dictData.addItem( index, line )
            self.pageData.tableData.addItem( index, line )
            index += 1

        self.loading = False

        self.scraperPage.updatePageData( self.pageData )


    # data changed on our page
    def viewDataChanged( self, viewData: ViewData ) -> None: 

        lines: list[str] = []
        self.pageData = viewData
    
        pageKeys = self.pageData.dictData.getKeys()
        for key in pageKeys:
        
            line = self.pageData.dictData.getItem( key )
            lines.append( line )

        FileOperation.createWriteLinesFileOp( self.inputFile, lines, self, False )


    # function must be implemented by derived class
    def fileOpComplete( self, fileOp: FileOperation ) -> None:

        if fileOp.handleError():
            return

        if fileOp.type == EFileOpType.eRead and fileOp.filepath == self.inputFile:
            self.parseUrls( fileOp )
            
        del fileOp 



    # see if our files changed
    def checkFileMonitor( self ) -> None:
       
        if self.fileMonitor.hasChanged():

            self.fileMonitor.resetChanged()
            self.readInputFile()




