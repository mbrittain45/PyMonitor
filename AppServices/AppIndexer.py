
import pickle

from AppDefs import DirDefs
from FileSystem import FileSystem


#
# AppIndexer - we keep track of indexes accross the entire application
#
class AppIndexer:

    newsEntryIndex = int(0)
    rssEntryIndex  = int(0)
    companyUID     = int(0)

    INDEXER_FILE   = DirDefs.makePath( DirDefs.APP_CACHE_PATH, "Indexes.dat" )

    # get the next news entry index
    @staticmethod
    def getNewsEntryIndex() -> int:

        if AppIndexer.newsEntryIndex == int(0):
            AppIndexer.readIndexesFromFile()
            
        AppIndexer.newsEntryIndex += 1
        return AppIndexer.newsEntryIndex


    # get the next news entry index
    @staticmethod
    def getRssEntryIndex() -> int:

        if AppIndexer.newsEntryIndex == int(0) and FileSystem.doesFileExist( AppIndexer.INDEXER_FILE ):
            AppIndexer.readIndexesFromFile()
        
        AppIndexer.rssEntryIndex += 1
        return AppIndexer.rssEntryIndex


    @staticmethod
    def getCompanyUid() -> int:

        if AppIndexer.companyUID == int(0) and FileSystem.doesFileExist( AppIndexer.INDEXER_FILE ):
            AppIndexer.readIndexesFromFile()
 
        AppIndexer.companyUID += 1
        return AppIndexer.companyUID
        
        

    # read indexes from our file
    @staticmethod
    def readIndexesFromFile():

        with open( AppIndexer.INDEXER_FILE, 'rb') as file:
            
            data = pickle.load(file)

            AppIndexer.newsEntryIndex = data['news_index']
            AppIndexer.rssEntryIndex  = data['rss_index']
            AppIndexer.companyUID     = data['company_uid']

    # todo: a task needs to write these values out occasionally

    # write indexes to our file
    @staticmethod
    def writeIndexesToFile():

        data = {
            'news_index': AppIndexer.newsEntryIndex,
            'rss_index': AppIndexer.rssEntryIndex,
            'company_uid': AppIndexer.companyUID
        }

        with open( AppIndexer.INDEXER_FILE, 'wb' ) as file:
            pickle.dump( data, file )


