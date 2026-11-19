

'''

import time

from Application import theApp
from Tasks import SimpleTask
from Shared import Mutex


#
# Search for Stocks in string in multiple tasks
#
class StockSearcher:
    

    #
    # task to search for all stocks in a string (news or rssfeed or twit or...)
    #
    class SearchTask( SimpleTask ):
        
        # init
        def __init__( self, parent, stringToSearch ):
            
            SimpleTask.__init__(self)
            
            self._stringToSearch = stringToSearch
            self._parent         = parent
            
            if self.__getAllStocks__():
                self.__startTask__()
            else:
                self.getClient().display( "Unable to Search for Stocks in Strings since the AllStocks dictionaries are empty" )
                self._finished  = True
                           

             
        # qrunnable function
        def run( self ):

            stockSymbols = self._allStocks.keys()
            for stockSymbol in stockSymbols:
            
                stockCompany = self._allStocks[ stockSymbol ].company
    
                if stockSymbol in self._stringToSearch or stockCompany in self._stringToSearch:
                    
                    locked = False
                    while locked  == False:
                        
                        locked = self.parent.resultsMutex.tryLock( 1 )
                        if locked:
                            self.parent.resultsList.append( ( self._stringToSearch, self._allStocks[ stockSymbol ] ) )
                        else:
                            time.sleep( .5 )

                    self.parent.resultsMutex.unlock()

            self.__setFinished__()
            
        


    # init
    def __init__( self, strList: list[str] ):
        
        self.resultsList     = []
        self._resultsMutex   = Mutex()
        self._tasks          = []
        
        # start a task for each string in strList
        for string in strList:
            self._tasks.append( StockSearcher.SearchTask( self, string ) )
            
            
    # see if all tasks are done
    def areTasksDone(self):
        
        for task in self._tasks:
            if task.isDone() == False:
                return False
 
        self._tasks.clear()
        return True
    




        

'''
