#

import datetime
from enum import Enum

from App import theStockApp

from AppDefs import DirDefs, Security, ViewData, ViewUser
from AppBaseTask import RepeatingTask, TaskParent
from AppUtils import GuardedList, TimeSensitiveRequestUrl, DTFmt
from FileSystem import FileSystem, FileOpParent, FileOperation
from AppServices import AppSecurities, AppAbbrvApi
from AppUI import GenericPage, PageFunctionData


#
# All Stocks Task - we'll use a git repository to pull all stocks/company names from
#
class AllStocksTask( RepeatingTask, FileOpParent, ViewUser ):

    ALL_STOCKS_DIR      = DirDefs.addToCacheDir( "ALL_STOCKS" )
    US_SYMBOLS_DIR      = DirDefs.makePath( ALL_STOCKS_DIR, "US_STOCKS" )
    
    US_GIT_CLONE_CMD    = "git clone https://github.com/rreichel3/US-Stock-Symbols.git"
    US_GIT_UPDATE_CMD   = "git --git-dir=" + US_SYMBOLS_DIR + " fetch origin"
    
    COMPANY_INFO_FILE   = DirDefs.makePath( ALL_STOCKS_DIR, "CompanyInfo_{}.txt" )   # one per week

    STOCKS_PAGE         = "All Stocks"
    TABLE_HDRS          = [ "UID", "Symbol", "Name", "Volume", "Previous Close", "Market Cap" ]
    Exchanges           = [ "nasdaq", "nyse" ]


    class EState( Enum ):
        eParseOurFile   = int(1)        # parse our file
        eMakeRequest    = int(2)        # get github project
        eReadFiles      = int(3)
        eParseFiles     = int(4)



    # init ourself
    def __init__( self, parent: TaskParent ):
        
        RepeatingTask.__init__( self, self.STOCKS_PAGE, parent )
        
        FileSystem.createDir( self.ALL_STOCKS_DIR )
        FileSystem.createDir( self.US_SYMBOLS_DIR )
           
        self.sleepTimeout   = int(1)
        self.procFilesCnt   = int(0)
        self.fileOps        = GuardedList()
        
        self.viewData       = ViewData( self.STOCKS_PAGE, self )
        
        # if our file exists and its only a week old use it
        if self.__createReadCompanyFile__():
            self.state      = self.EState.eParseOurFile
        else:
            self.state      = self.EState.eMakeRequest

        # create our page
        pageFuncData        = PageFunctionData( AppAbbrvApi.getMainWidget(), self.STOCKS_PAGE, 2, self.TABLE_HDRS )
        
        pageFuncData.rowDeletable       = True
        pageFuncData.rowHideable        = True
        pageFuncData.columnReordering   = True

        # todo: row pages
        
        self.allStocksPage  = GenericPage( pageFuncData ) 
        AppAbbrvApi.getMainWidget().addTab( self.allStocksPage, self.STOCKS_PAGE )   # type: ignore

        self.__startTask__()


# todo: persist hidden and deleted pages, columns, rows...


    def __createReadCompanyFile__( self ) -> bool:

        today    = datetime.date.today()
        weekNum  = today.isocalendar().week  # Python 3.9+
        filepath =  self.COMPANY_INFO_FILE.format( weekNum )
        if FileSystem.doesFileExist( filepath ):
            FileOperation.createReadLinesFileOp( filepath, self, False )    
            return True
        return False



    # make the url request
    def __makeRequest__(self):

        if not FileSystem.doesDirExist( self.US_SYMBOLS_DIR ):
            data_tuple = TimeSensitiveRequestUrl.get( self.US_GIT_CLONE_CMD )
        else:
            data_tuple = TimeSensitiveRequestUrl.get( self.US_GIT_UPDATE_CMD )
        return data_tuple[0]



    # file operation callback
    def fileOpComplete( self, fileOp: FileOperation ):

        if fileOp.handleError():
            return
        self.fileOps.addItem( fileOp )
      

                
     # our processing task thread function
    def processTask(self) -> bool:

        self.cycleCount += 1

        if self.state == self.EState.eParseOurFile:

            if self.cycleCount > 3:
                self.state = self.EState.eMakeRequest
            else:

                if self.fileOps.getCount():
                    self.parseCompanyFile( self.fileOps.popHead() )
                    theStockApp.setInitialized( True )                    
                    self.repeat = False
                        
        else:
            return self.handleGitHubFiles()

        return True

            


    # handle github file processing
    def handleGitHubFiles( self ) -> bool:

        self.cycleCount += 1
        
        if self.state == self.EState.eMakeRequest:
             
            self.cycleCount = 0
            
            if not self.__makeRequest__():
                    
                if self.errorCnt > 0:
                    self.repeat = False
                    # todo:theStockApp.setUnableToInitialize()
                    return False
                       
                self.error = "AllStocksTask request to GitHub failed"
                return False
                
            self.state = self.EState.eReadFiles
            
        elif self.state == self.EState.eReadFiles:
            
            files = FileSystem.findFiles( self.US_SYMBOLS_DIR, ".json" )
            if len( files ) > 2:        

                for file in files:
                    FileOperation.createReadLinesFileOp( file, self, False ) 

                self.state = self.EState.eParseFiles

        elif self.state == self.EState.eParseFiles:

            if self.fileOps.getCount() > 0:
                self.processFileReadOps()
            
            if self.procFilesCnt > 3:   # we are done
                self.repeat = False
                
            if self.cycleCount > 3:
                return self.readOldCompanyFile()

        return True



    # find and read an old company file
    def readOldCompanyFile( self ):

        cnt     = 0
        today   = datetime.date.today()
        weekNum = today.isocalendar().week  # Python 3.9+

        while cnt < 10:

            filepath =  self.COMPANY_INFO_FILE.format( weekNum )
            
            if FileSystem.doesFileExist( filepath ):
                FileOperation.createReadLinesFileOp( filepath, self, False )    # type: ignore
                self.state = self.EState.eParseOurFile
                return True
                    
            weekNum -= 1
            cnt += 1

        self.repeat = False
        self.error = "Unable to find a Company File To Parse"
        # todo:theStockApp.setUnableToInitialize()
        return False
 



    # if changed rewrite our backup file
    def viewDataChanged( self, viewData: ViewData ) -> None:    # type: ignore
        assert( False )        
        # todo:


    # process file data and make sure we got all the data
    def processFileReadOps( self ):

        if self.fileOps.getCount() <= 0:
            return

        while self.fileOps.getCount():

            self.procFilesCnt += 1
        
            fileOp: FileOperation = self.fileOps.popHead()             
      
            stockDefs     = fileOp.data.blob.split( "}," )
            for stockDef in stockDefs:
                stock = Security()  
                stock.parseJsonText( stockDef.split( "," ) )
                self.viewData.dictData.addItem( stock.uid, stock )

        AppSecurities.setStocks( self.viewData.dictData ) 

        self.updatePage()


    # write our company file
    def writeCompanyFile( self ):

        blob = ""
        stockKeys = self.viewData.dictData.getKeys()
        for stockKey in stockKeys:
            stock: Security = self.viewData.dictData.getItem( stockKey ) # no actual list just one security item
            blob += stock.toFileFmt()
        
        FileOperation.createWriteBlobFileOp( self.COMPANY_INFO_FILE.format( DTFmt.getMonth() ), blob, self, False )    # type: ignore
        

    # parse our company file                   
    def parseCompanyFile( self, fileOp: FileOperation ):
        
        while len( fileOp.data.blob ) > 0:

            stock = Security()
            stock.fromFileFmt( fileOp.data.blob )

            self.viewData.dictData.addItem( stock.uid, stock )
            
        self.updatePage()
        
        

    # update our page view
    def updatePage( self ):

        self.viewData.tableData.clear()

        stockKeys = self.viewData.dictData.getKeys()
        for stockKey in stockKeys:
            stock: Security = self.viewData.dictData.getItem( stockKey ) # no actual list just one security item

            row: list[str] = stock.getTableRow()    
            
            self.viewData.tableData.addItems( stock.uid, row )

        self.allStocksPage.updatePageData( self.viewData )



    