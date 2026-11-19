

from AppBaseTask import RepeatingTask, TaskParent
from AppServices import HyperlinkTracker, AppIndexer


#
# Update Task - we go around and ever service that needs a file saved every so often and have them save their data
#
class UpdateTask( RepeatingTask ):


    def __init__( self, parent: TaskParent ):

        RepeatingTask.__init__( self, "UpdatingTask", parent )
        self.sleepTimout = int(5)
        self.__startTask__()


    def processTask( self ) -> bool:  

        htracker = HyperlinkTracker()
        htracker.writeHyperlinksFile()
       
        del htracker

        AppIndexer.writeIndexesToFile()

        #self.persistUIPageData()

        return True