

import requests

from AppUtils import Logger
from AppServices import UrlRequestTracker
from FileSystem import FileOperation, FileOpParent

       # maryanne 326-209-0771
#
# Request a specific Url
#
class RequestUrl:

    @staticmethod
    def processError( rsp: requests.Response, url: str ):

        if rsp.status_code == 404:
            Logger.err( f"Resource not found for url request: {url}" )

        elif rsp.status_code >= 400 and rsp.status_code < 500:
            Logger.err( f"Client error: {rsp.status_code} for url: {url}" )

        elif rsp.status_code >= 500 and rsp.status_code < 600:
            Logger.err( f"Server error: {rsp.status_code} for url: {url}" )

        else:
            Logger.err( f"Unexpected status code: {rsp.status_code} for url: {url}" )



    @staticmethod
    def __getUrl__( url: str ) -> tuple[ bool, requests.Response ]:
        
        rsp = requests.get( url, timeout=15 )
        
        Logger.einfo( ("Request: " + url) )
        Logger.einfo( ("Response: " + rsp) ) # type: ignore

        #print( "CONTENT: " + rsp.content)
        #print("TEXT:  " + resp.content)
        
        if rsp.status_code == 200:
            return (True, rsp)
        else:
            RequestUrl.processError( rsp, url )
      
        return (False, rsp)
        


    @staticmethod
    def __requestAndSave__( url: str, filePath: str, parent: FileOpParent ) -> tuple[ bool, requests.Response ]:
        
        rsp = requests.get( url, timeout=15 )
        
        if __debug__:
            Logger.einfo( ("Request: " + url) )
            Logger.einfo( ("Response: " + rsp) ) # type: ignore

        
        if rsp.status_code == 200:
   
            FileOperation.createWriteBlobFileOp( filePath, rsp.text, parent, False )
            return (True, rsp)
        else:
            RequestUrl.processError( rsp, url )
            
        return (False, rsp)



#
# TimeSensitiveRequestUrl - always make a fresh request for the url
# 
class TimeSensitiveRequestUrl( RequestUrl ):

    # request a url and return the response and if its valid or not
    @staticmethod
    def get( url: str ) -> tuple[ bool, requests.Response ]:
    
        return RequestUrl.__getUrl__( url )


    # request a url and return the response and if its valid or not
    @staticmethod
    def requestAndSave( url: str, filePath: str, parent: FileOpParent ) -> tuple[ bool, requests.Response ]:
            
        return RequestUrl.__requestAndSave__( url, filePath, parent )




#
# TimeInsensitiveRequestUrl - request a URL, if we have a cached response for the requested url that is only
#   a few hours old you'll get the cached response.
# 
class TimeInsensitiveRequestUrl( RequestUrl ):

    # request a url and return the response and if its valid or not
    @staticmethod
    def get( url: str ) -> tuple[ bool, requests.Response ]:
    
        if UrlRequestTracker.hasUrl( url ):
 
            response = UrlRequestTracker.getUrlResponse( url )
            if response.status_code == 200:
                return tuple[ True, response ]      # type: ignore
 
        data_tuple = RequestUrl.__getUrl__( url )
        if data_tuple[0]:
            UrlRequestTracker.saveResponse( url, data_tuple[1] ) 
            
        return data_tuple


    # request a url and return the response and if its valid or not
    @staticmethod
    def requestAndSave( url: str, filePath: str, parent: FileOpParent ) -> tuple[ bool, requests.Response ]:
            
        return RequestUrl.__requestAndSave__( url, filePath, parent )

