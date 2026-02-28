

import requests

from AppUtils import Logger


'''
#
# Iterator object - forward iterator w/ previous value retrieval only
#
class Iterator:
    
    # init ourself
    def __init__( self, iterVals, endVal = "END" ):
        self.iter    = iter( iterVals, endVal )
        self.endVal  = endVal
        self.nextVal = None
        self.prevVal = None
        
    # iterate forward
    def getNext(self):
        self.prevVal = self.iter
        self.nextVal = next( self.iter, self.endVal )
        return self.nextVal
    
    # get previous value
    def getPrevious(self):
        return self.prevVal
    
    # see if its the end
    def isEnd(self):
        if self.nextVal == self.endVal:
            return True
        return False
'''



        

#
# Request a specific Url
#
class RequestUrl:
    
    # request a url and return the response and if its valid or not
    @staticmethod
    def get( url: str ) -> tuple[ requests.Response, bool ]:
        
        rsp = requests.get( url, timeout=15 )
        
        Logger.einfo( ("Request: " + url) )
        Logger.einfo( ("Response: " + rsp) ) # type: ignore

        #print( "CONTENT: " + rsp.content)
        #print("TEXT:  " + resp.content)
        
        if rsp.status_code == 200:
            return rsp, True

        elif rsp.status_code == 404:
            Logger.err( f"Resource not found for url request: {url}" )
        elif rsp.status_code >= 400 and rsp.status_code < 500:
            Logger.err( f"Client error: {rsp.status_code} for url: {url}" )
        elif rsp.status_code >= 500 and rsp.status_code < 600:
            Logger.err( f"Server error: {rsp.status_code} for url: {url}" )
        else:
            Logger.err( f"Unexpected status code: {rsp.status_code} for url: {url}" )
            
        return rsp, False
        


        