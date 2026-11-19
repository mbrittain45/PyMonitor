

from enum import Enum

from AppUtils import GuardedList
from FileSystem import FileOperation, FileOpParent

from AppBaseTask import Task, FuncPtrTask
from AppServices import AppSecurities

from AppBaseTask import TaskParent, RepeatingTask
from AppUtils import GuardedQueue
from AppDefs import  NewsEntry


# mining result match new entry type
class EMiningResult( Enum ):

    eCompany    = int(0)
    eSymbol     = int(1)
    eOther      = int(2)


'''
#
# Mining Results - found matches to the news entry
#
class MiningResults:

    def __init__(self, type: EMiningResult ):

        self.type           = type
        self.companies      = GuardedList()
        self.goverments     = GuardedList()
        self.others         = GuardedList()
'''


#
# News Mining Task - mine the news entries for company names, stock symbols and sentiment analysis
#
class NewsMiningTask( RepeatingTask, FileOpParent ):


    newsQueue    = GuardedQueue()
        

    # init ourself
    def __init__( self, parent: TaskParent  ):

        RepeatingTask.__init__( self, "NewsMiningTask", parent )

        self.newStoryBlob = ""
        self.newsTask     = None

        self.sleepTime    = int(2)
        
        self.stockSymbols = AppSecurities.getStockSymbols()
        self.companyNames = AppSecurities.getCompanyNames()
        #self.miscTerms   = theApp.getMiscSearchTerms() # todo:

        self.__startTask__()


    # queue a news entry
    @staticmethod
    def queueNewsEntry( newsEntry: NewsEntry ):
        NewsMiningTask.newsQueue.addTail( newsEntry )



   # function must be implemented by derived class
    def fileOpComplete(self, fileOp: FileOperation ) -> None:

        if fileOp.handleError():
            return
        else:
            self.newStoryBlob = fileOp.data.blob

        del fileOp



    # process our task - mining the news for gold
    def processTask(self) -> bool:

        if self.newsQueue.getCount() <= 0:
            return True
        
        if self.newsTask == None and self.newsQueue.getCount():

            news = self.newsQueue.popHead()
            FileOperation.createReadBlobFileOp( news.storyFilePath, self, False )
            FuncPtrTask( "searchNewsEntry1", self, self.searchNewsEntry, [news, self.stockSymbols] )      # type: ignore
            FuncPtrTask( "searchNewsEntry2", self, self.searchNewsEntry, [news, self.companyNames] )      # type: ignore

        return True


    # callback when task is complete
    def taskComplete( self, task: Task ):

        # todo: pass to the next stage
        

        if task is self.newsTask:       # type: ignore
            self.newsTask = None
        
        del task


    # check news for keyword
    def searchNewsEntry( self, inputTuple: tuple[NewsEntry, list[str]] ) -> None:

        newsEntry       = inputTuple[0]
        searchTerms     = inputTuple[1]
        foundTerms      = GuardedList()

        for term in searchTerms:

            if newsEntry.summary.lower().find( term.lower() ) != -1:
                foundTerms.addItem( term )

            if newsEntry.title.lower().find( term.lower() ) != -1:
                foundTerms.addItem( term )

        for term in searchTerms:

            if self.newStoryBlob.lower().find( term ) != -1:
                foundTerms.addItem( term )

        newsEntry.miningMatches.appendList( foundTerms.copyList() )
        


