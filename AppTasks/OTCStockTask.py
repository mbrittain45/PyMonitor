
'''
from AppTasks import Task

from AppDefs import Defs

from AppUtils import DTUtils, DirectoryOps, Dictionary

from AppTasks import EtaskResult


#
# OTC Stock - an opver the counter stock
#
class OTCStock:

    # init ourself
    def __init__( self, url = "", symbol = "" ):

        self.url           = url
        self.symbol        = symbol
        self.price         = float(0)
        self.lastRequest   = Epocher.getTime()
        self.priceChange   = float(0)
        self.lastChange    = Epocher.getTime()


    # parse our line from the otc stock task file
    def parse( self, line ):

        vals = line.split( Defs.COM_DEL )
       
        self.url        = vals[0]
        self.symbol     = vals[1]
        self.price      = vals[2]
        self.lastChange = vals[3]


    # buffer ourself for writing to a file
    def buffer( self ):

        return (self.url + Defs.COM_DEL + self.symbol + Defs.COM_DEL + self.price + Defs.COM_DEL + self.lastPriceChange + Defs.END_DEL)
    



#
# OTC Stock Task - we keep track of OTC stocks
#   which we scan for occasionally
#
class OTCStockTask( Task ):

    OUTPUT_DIR     = Defs.addToCacheDir( "OTCStocks" )
    OUTPUT1_FILE   = Defs.makePath( OUTPUT_DIR, "OTCStocks.dat" )
    OUTPUT2_FILE   = Defs.makePath( OUTPUT_DIR, "DeadOTCStocks.dat" )

    # init
    def __init__( self ):

        DirectoryOps.createDir( self.OUTPUT_DIR )

        Task.__init__( self, "OTC Stock Task", True, self )

        self._sleepTime     = int(10) # sleep 10 minutes at a time

        self._otcStocks     = Dictionary()
        self._deadOtcStocks = Dictionary()
        self._newStocks     = int(0)

        #FunctionTask( FuncPtrDef( self.readOutputFile ), self )
        self.readOutputFile()


    # process the task
    def processTask(self):

        # make sure we have something to process
        if self._otcStocks.keys().count() <= 0:
            return ETaskResult.eSucceeded

        stockKeys   = self._otcStocks.keys()
        for stockKey in stockKeys:
            
            otcStock = self._otcStocks[ stockKey ]
        
            if otcStock.lastRequest > (DTUtils.getCurTime() - timedelta( days=2 )):

                # todo:
                #resp = RequestURL( otcStock.url )
                #if resp != None:
                #                    self.parsePrice( resp )


        return ETaskResult.eSucceeded
        


    # add an OTC Stock
    def addOTCStock( self, stockUrl, symbol )

        stock = self._otcStocks[ symbol ]
        if stock == None:
      
            self._otcStocks[ symbol ] = OTCStock( stockUrl, symbol )
            self._newStocks += 1

            if self._newStocks > 10:
                FunctionTask( FuncPtrDef( self.writeOutputFile ), self )



    # read our output file
    def readOutputFile( self ):

        lines = TextFile.read( self.OUTPUT1_FILE, True )

        for line in lines:

           otcStock = OTCStock()
           otcStock.parse( line )

           self._otcStocks[ otcStock.symbol ] = otcStock


    # write our output file
    def writeOutputFile( self ):

        buffer      = ""
        stockKeys   = self._otcStocks.keys()
        
        for stockKey in stockKeys:
            otcStock = self._otcStocks[ stockKey ]
            buffer   += otcStock.buffer()

        TextFile.write( self.OUTPUT1_FILE, buffer, True )


    # called when our function tasks are done
    def taskComplete( self, task ):

        del task
        task = None


'''