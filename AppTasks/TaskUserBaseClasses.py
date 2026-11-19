

'''

from Shared import Dictionary
from Tasks import BaseThread


#
# Awaiting All Stocks to become valid
#
class AwaitingAllStocksValidity:

    # init
    def __init__( self ):

        self.copyOfAllKnownStocks   = Dictionary()
        self._awaitingTask          = None


    # call when all stocks are valid - should be overridden
    def allStocksAreValid( self ):

        # function should be overridden
        assert( False )
        assert( self == None )




#
# Thread Processor base class
# 
class ThreadProcessor:

    # init
    def __init__( self, parent ):

        self._parent        = parent
        self._baseThread    = None


    # thread processing function must be overridden
    def performProcessing( self ):

        assert( False )

        
    # set our base thread object
    def setBaseThread( self, baseThread: BaseThread ):

        self._baseThread = baseThread

'''