
'''


from AppUtils import GuardedQueue, GuardedDictionary

from AppTasks import Task, FunctionPtrTask, FuncPtrDef, ETaskResult

# todo: what is the findWhat need to list topics like earning, book value, ..what ?


#
# HistoricalRequest
#
class HistoricalRequest:

    def __init__( self, company, ticker, startTime, endTime, findWhat, requestor ):

        self.company    = company
        self.ticker     = ticker
        self.startTime  = startTime
        self.endTime    = endTime
        self.whatToFind = findWhat
        self.requestor  = requestor




#
# Historical Task - searches our archive for historical data related to a specific company topic, which is the findWhat question
# 
# all users of a HistrocalRequest need to implement - historicalRequestComplete() so we have somewhere to put the results
# 
class HistoricalTask( Task ):


    # init
    def __init__( self, parent ):

        Task.__init__( "HistoricalTask", True, parent )

        self.requestQueue       = GuardedQueue()
        self.processingQueue    = GuardedDictionary()

        self._sleepTime         = int(2)

        self.__startTask__()


    # add a new historical request
    def queueRequest( self, request: HistoricalRequest ):
        self.requestQueue.addItem( request )


    # our task processing function
    def processTask( self ) -> bool:

        if self.requestQueue.getCount() <= 0:
            return True

        request = self.requestQueue.getItem()

        self.processingQueue.addItem( id(request), request )
        
        FunctionPtrTask( FuncPtrDef( self.processRequest, request ), self )

        return True
   
    

'''