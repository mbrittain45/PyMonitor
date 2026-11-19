

'''


from App import theApp, ViewObjectUpdate, NewsEntry, Defs
from AppTasks.BaseTask import Task, ETaskResult
from AppTasks.TaskUtils import RepeatingTask, FunctionPtrTask, SentimentAnalyzer
from AppUtils import Log, TextFile, GuardedDictionary, GuardedDictionaryList, StrUtils


#
# Mining Results Task - process the news mining results for sentiment analysis
#
class MiningResultsTask( RepeatingTask ):

    # init ourself
    def __init__( self ):

        RepeatingTask.__init__(self, "MiningResultsTask", theApp.getTaskMgr() )
        self._processQueue     = GuardedDictionaryList()
        self._sleepTime        = int(3)
        self.__startTask__()


    # queue the results
    def queueResults( self, miningResults: GuardedDictionaryList ):

        keys = miningResults.getKeys()
        for key in keys:
            valueList = miningResults.popItems( key )
            self._processQueue.addItem( key, valueList )
            
               

    # process our task - getting the sentiment analysis for the news mining results
    def processTask(self) -> bool:

        if self._processQueue.getKeys().count() <= 0:
            return True
        
        NumToProcess = self._processQueue.getKeys().count()
        if NumToProcess > 10:
            NumToProcess = int(10)

        ikey        = int(0)
        companyKeys = self._processQueue.getKeys()
        while ikey < NumToProcess:

            companyNews = self._processQueue.popItems( companyKeys[ ikey ] )

            for newsEntry in companyNews:

                story = TextFile.read( newsEntry.storyFilePath, True )
                if len(story) < len(newsEntry.summary):
                    story = newsEntry.summary

                analyzer                    = SentimentAnalyzer()
                sentences                   = StrUtils.parseSentences( story )
                newsEntry.sentimentScore    = analyzer.getSentiment( analyzer.stripStopWords( sentences ) )
                
                theApp.getTaskMgr().getUpdateViewTask().updateView( ViewObjectUpdate( Defs.EViewType.eNewsSentiment, newsEntry ) )

                del analyzer
           
            ikey += companyNews.count()

        return False
 


'''