

''' todo:

from App import theApp

from AppDefs import Defs, ViewUpdate, NewsEntry

from AppUtils import DirectoryOps, FileOps, TextFile, DTUtils, RequestUrl

from AppTasks import BaseFeedTask, FunctionTask, FuncPtrDef, ETaskResult


#
# Website data used to control how we request data from a given site
#
class YahooWebsiteData:

    # our local copy of a robots.txt file from the specific website
    LOCAL_ROBOTS_FILE  = "RobotsDotText_{}_On{}.txt"
    

    #
    # init ourself
    #
    def __init__(self, outputDir: str, website: str):

        self._workingDir          = outputDir
        self._websiteURL          = website
        self._robotsTextFileText  = ""  
        self._savedRobotFilePath  = ""  
        self._robotFileDate       = Epocher.getDate()

        self._siteMapURLs         = []
        self._stockURLs           = []
                
        # replace once tested
        #FunctionTask( FuncPtrDef( self.findLocalRobotFile ), self )
        self.__findOurLocalRobotsFile__()
               

    #
    # scan the website for data
    #
    def scanWebsite( self ):

        FunctionTask( FuncPtrDef( self.performWebsiteScan ), self )


    #
    # perform the actual website scan
    #
    def performWebsiteScan( self ):

        # see if we need a robots.txt file
        if self.__isRobotFileNeeded__():
            self.__requestRobotFile__()

        # request each sitemap url
        self.__requestSitemaps__()

        # request each site url
        self.__requestStockURLs__()

        # todo: what to do with the data


    #
    # request the stock specific urls
    #
    def __requestStockURLs__( self ):

        for stockUrl in self._stockURLs:
            
            p1 = stockUrl.find( "/quote/" )
            p2 = stockUrl.find( "/summary/" )
            p1 += len( "/quote/" )
            
            symbol = stockUrl[ p1 : p2 ]

            # see if the symbol is a stock off a major index
            if theApp.isMajorIndexStockSymbol( symbol ):


            else:
                # else its an OTC stock so pass it off to the OTC task
                theApp.getTaskMgr().getOTCTask().addOTCStock( stockUrl, symbol )





    #
    # request each sitemap url
    #
    # response format hundreds of xml urls:
    #
    # <url>
    #   <loc>https://finance.yahoo.com/quote/A6T.HA/history/</loc>
    #   <lastmod>2022-12-29T18:48:49.406Z</lastmod>
    #   <changefreq>daily</changefreq>
    #   <priority>0.8</priority>
    # </url>
    #
    def __requestSitemaps__( self ):

        for url in self._siteMapURLs:

            resp = RequestUrl.get( url )
            if resp != None:

                tmp = resp
                while len( tmp ) > 0:

                    xmlObj = BaseHtmlParser.getTag( tmp, "url" )
                    url    = BaseHtmlParser.getTag( xmlObj, "loc" ) 

                    if url.find( "/summary/" ) != -1:
                        self._stockURLs.append( url )

                    hp    = (tmp.find( "</url>" ) + int(6))
                    tmp   = tmp[ hp, (len( tmp ) - hp) ]


    #
    # request the robots.txt file
    # 
    def __requestRobotsFile__( self ):

        resp = RequestUrl.get( self._websiteURL + "/Robots.txt" )
        if resp != None:

            # save the robots.txt file locally
            self.__saveLocalRobotsFile__( resp )
            # parse the response
            self.__parseRobotFileText__( resp )


    #
    # find our local robots file for this website - run as a task
    #
    def __findLocalRobotFile__( self ):

        filePath = FileOps.findFileName( self._workingDir, StrUtils.getWebsiteName( self._websiteURL ) )
        if len(filePath) > 0:
            
            # save the file path
            self._savedRobotFilePath = filePath
            
            # read the saved file
            self.__readSavedRobotFile__( filePath )


    #
    # read our locally saved robots file 
    #
    def __readSavedRobotFile__( self, filePath ):

        # parse the text file lines
        self.__parseLocalRobotFile__( TextFile.read( filePath, True ) )

        # parse the date off the local robot file path
        self._robotFileDate = DTUtils.parseFileDT( filePath[ filePath.find( "_On" ) : filePath.find( ".txt" ) ] )


    #
    # parse our local robots.txt file w/ a different name
    #
    def __parseRobotFileText__( self, fileLines ):

        for line in fileLines:

            tmp = line.lower()
            p   = tmp.find( "sitemap" )
            
            if p != -1:
                p  += 8
                self._siteMapURLs.append( line[ p : len(tmp) - p2 ].strip() )


    #
    # see if we need to read the robots.txt file
    #
    def __isRobotFileNeeded__( self ):

        # if the site map urls are empty read the robots file
        if self._siteMapURLs.count() < 1:
            return True
        
        # otherwise if its been a week read it again
        if self._robotFileDate < (DTUtils.getCurTime() - timedelta(days=7)):
            return True
        
        return False

        
    #
    # save our local robots file
    #
    def __saveLocalRobotsFile__( self, text: str ):

        # if we have an old local robots file delete it
        if len(self._savedRobotFile) > 0:
        
            FileOps.removeFile( self._savedRobotFile )
            self._savedRobotFile = ""
            self._robotFileDate  = Epocher.getDate()

        # set the date of local robots file and path
        self._robotFileDate = DTUtils.getDate()
        self._savedRobotFile = (self.workingDir + self.ROBOT_FILE.format( self.getWebsiteName(), DTUtils.getFileDateMarker() ))
        
        TextFile.write( self._savedRobotFile, text, True )


    #
    # called when our function tasks are done
    #
    def taskComplete( self, task ):
        
        del task
        task = None


'''