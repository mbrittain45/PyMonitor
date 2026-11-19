
import requests

from AppDefs import DirDefs, Defs
from FileSystem import FileSystem
from AppUtils import GuardedDictionary, DTUtils
from AppServices import HttpResponseSerializer


#
# Url Request Tracker - tracks all requested urls so we aren't repeatedly calling a url across tasks
#
class UrlRequestTracker():

    OUTPUT_DIR = DirDefs.addToCacheDir( "URLRequestCache" )

    requestedUrls = GuardedDictionary() # hold the url as the key and response as the value
    
    # todo: must be called at AppStartup

    # cleanse and create our directory
    @staticmethod
    def createDirectory() -> None:

        FileSystem.deleteDirs( UrlRequestTracker.OUTPUT_DIR )
        FileSystem.createDirs( UrlRequestTracker.OUTPUT_DIR )


    # get the url file path
    @staticmethod
    def __getUrlFilePath__( url: str ) -> str:
       
        return (UrlRequestTracker.OUTPUT_DIR + url + Defs.DATEXT)


    # see if a url has been requested
    @staticmethod
    def hasUrl( url: str ) -> bool:    # type: ignore
        
        return UrlRequestTracker.requestedUrls.hasItem( url )         # type: ignore


    # get the requested url response if it was recent 
    @staticmethod
    def getUrlResponse( url: str ) -> requests.Response:      # type: ignore

        data_tuple = HttpResponseSerializer.readResponseFromFile( UrlRequestTracker.__getUrlFilePath__( url ) )    # type: ignore

        response = data_tuple[0]        # type: ignore
        datetime = data_tuple[1]        # type: ignore

        if DTUtils.isWithinTimeRange( datetime, int(6) ):  
            return response                       

        UrlRequestTracker.requestedUrls.popItem( url )
        FileSystem.deleteFile( UrlRequestTracker.__getUrlFilePath__( url ) )
        
        return requests.Response()


    # save a request and response to a file        
    @staticmethod
    def saveResponse( url: str, response: requests.Response ) -> None:    # type: ignore

        UrlRequestTracker.requestedUrls.addItem( url, response )        # type: ignore

        HttpResponseSerializer.writeResponseToFile( UrlRequestTracker.__getUrlFilePath__( url ), response )    # type: ignore


