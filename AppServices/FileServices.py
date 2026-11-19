

'''

ViewDataUser


   # compress a directory for a task at a certain time
    #def compressDir( self, dirName: str, compressAfterTime: datetime ):
    #   self._dirsToCompress.addItem( dirName, compressAfterTime )



void MyMainWidget::commitData(QSessionManager& manager)
{
    if (manager.allowsInteraction()) {
        int ret = QMessageBox::warning(
                    mainWindow,
                    tr("My Application"),
                    tr("Save changes to document?"),
                    QMessageBox::Save | QMessageBox::Discard | QMessageBox::Cancel);

        switch (ret) {
        case QMessageBox::Save:
            manager.release();
            if (!saveDocument())
                manager.cancel();
            break;
        case QMessageBox::Discard:
            break;
        case QMessageBox::Cancel:
        default:
            manager.cancel();
        }
    } else {
        // we did not get permission to interact, then
        // do something reasonable instead
    }
}


    @Slot()
    def appLastWndClosedSlot( ):
        # todo: Logger.writeLog( "Exiting Application" )
        exit( 0 );
        
    @Slot()
    def appScreenChangedSlot( screen : QScreen ):
        assert( screen )
        assert( False )

    @Slot()
    def appSaveStateSlot( mgr: QSessionManager ):
        assert( mgr )
        assert( False )

#void	focusObjectChanged(QObject *focusObject)
#void	focusWindowChanged(QWindow *focusWindow)
#void	primaryScreenChanged(QScreen *screen)

   
#    def getReporter(self):
#        return self._reporter 
 

    # compress a directory for a task at a certain time
    #def compressDir( self, dirName: str, compressAfterTime: datetime ):
    #   self._dirsToCompress.addItem( dirName, compressAfterTime )


    def pauseApplication(self, pause: bool ) -> None:
        
        self.appPaused = pause
        if not self.appPaused:
            self.taskManager.startWaitingTasks()
        

    def isApplicationPaused( self ) -> bool:
        return self.appPaused
        
        
    # get the main window
    def getWnd(self):
        return self._theWnd


    def getStatusBar( self ):
        self.mainWindow.getStatusBar()

        # create our other dictionaries
        FunctionPtrTask( "CreateOtherDictionaries", self, self.createDictionaries )

        # write out our companies file
        FunctionPtrTask( "WriteCompaniesFile", self, self.writeCompaniesFile )

        # write out our statistics companies file
        FunctionPtrTask( "WriteDailyStatistics", self, self.writeDailyStatistics )
    

    # write out our companies file
    def writeCompaniesFile( self ):

        buffer = ""
        companyKeys = self._companiesByName.getKeys()
        for companyKey in companyKeys:
            buffer += self._companiesByName[ companyKey ].formatDailyCompanyInfo( True )

        TextFile.queueWriteFile( self.APP_STOCKS_FILE, buffer, False )
    

    # read our companies file
    def readCompaniesFile( self ):

        text = TextFile.read( self.APP_STOCKS_FILE, False )
        while len( text ) > 0:
            companyInfo = DailyCompanyInfo()
            text        = companyInfo.parse( text )

            self._companiesByName[ companyInfo.getName() ] = companyInfo

        FunctionPtrTask( "createDictionaries", self, self.createDictionaries )



    # create our other dictionaries
    def createDictionaries( self ):
    
        companyNameKeys = self._companiesByName.getKeys()
        for companyName in companyNameKeys:

            companyInfo = self._companiesByName[ companyName ]

            self._companiesByTicker[ companyInfo.getSymbol() ]  = companyInfo
            self._companiesByUid[ companyInfo.getUid() ]        = companyInfo

            if companyInfo.exchange == "amex":
                self._companiesByExchange[ "amex" ].append( companyInfo )
            elif companyInfo.exchange == "nyse":
                self._companiesByExchange[ "nyse" ].append( companyInfo )
            else:
                self._companiesByExchange[ "nasdaq" ].append( companyInfo )

        headers = [ ]


        centralWidget = theStockApp.getMainWindow().getCentralWidget()

        amexPage = GenericTablePage( centralWidget, "AMEX Exchange Page", 2, False, headers )
        nysePage = GenericTablePage( centralWidget, "NYSE Exchange Page", 2, False, headers )
        amexPage = GenericTablePage( centralWidget, "Nasdaq Exchange Page", 2, False, headers )

        centralWidget.addTab( TaskStatusPage(), "AMEX Exchange" )
        centralWidget.addTab( TaskStatusPage(), "NYSE Exchange" )
        centralWidget.addTab( TaskStatusPage(), "Nasdaq Exchange" )
 
        amexView = ViewData( "AMEX Exchange", headers, self )
        amexView.setDictData( self._companiesByExchange[ "amex" ] )
        theApp.getTaskMgr().updateView( amexView )

        nyseView = ViewData( "NYSE Exchange", headers, self )
        nyseView.setDictData( self._companiesByExchange[ "nyse" ] )
        theApp.getTaskMgr().updateView( nyseView )

        nasdaqView = ViewData( "NASDAQ Exchange", headers, self )
        nasdaqView.setDictData( self._companiesByExchange[ "nasdaq" ] )
        theApp.getTaskMgr().updateView( nasdaqView )

        theStockApp.setInitialized( True ) 



    # write out file for the daily statistics getAllStocks retrieved by the month
    def writeDailyStatistics( self ):

        buffer      = DTUtils.getInFileDT()
        
        companyKeys = self._companiesByName.getKeys()
        for companyKey in companyKeys:
            buffer += self._companiesByName[ companyKey ].formatDailyCompanyInfo( False )

        TextFile.queueAppendFile( self.APP_STATS_FILE.format( DTUtils.getMonth() ), buffer, False )


    # todo:
    # read our daily statistics for a given month
    def readDailyStatistics( self, month: int ):
    
        timestampedStats = GuardedDictionaryList()

        if FileOps.doesFileExist( self.APP_STATS_FILE.format( month ) ):

            text = TextFile.read( self.APP_STATS_FILE.format( month ), False )
            
            timestampDict = DTUtils.parseInFileDT( text )

            timestamps    = timestampDict.getKeys()
            for timestamp in timestamps:

                blob = timestampDict[ timestamp ]

                while len( blob ) > 0:

                    stats = DailyCompanyStats()
                    blob  = stats.parseStats( blob )

                    timestampedStats.addItem( timestamp, stats )

        return timestampedStats

   '''
    

 
 






