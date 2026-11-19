

''' todo:

from App import theApp, Defs, ViewUpdate
from AppUI import TableWidget, TaskStatusTableWidget
from AppTasks import FunctionPtrTask


#
# URLs Table Widget
#
class URLTableWidget( TableWidget ):
    
    TableHeaders = [ "Request URLs" ]
    
    # init
    def __init__(  self, viewType: Defs.EViewType, uiLevel: int ):

        TableWidget.__init__( self, viewType, uiLevel, self.TableHeaders )
        self.itemChanged.connect(self.handleItemChanged)


    # handle an item changing
    def handleItemChanged( self, item ):

        row         = item.row()
        newText     = item.text()

        if row < self.lastUpdate.listData.count():
            self.lastUpdate.listData[ row ] = newText 
        else:
            self.lastUpdate.listData.append( newText )

        if self.lastUpdate.viewType == Defs.EViewType.eNewsFeedUrls:
            theApp.getTaskMgr().getNewsFeedTask().updateUrlsFile( self.lastUpdate )
        else:
            theApp.getTaskMgr().getRssFeedTask().updateUrlsFile( self.lastUpdate )


         
    # set the urls for display
    def displayUrls( self ):
        
        self.setUpdatesEnabled(False)
        self.clear()
        
        assert( self.viewUpdate.isList() )

        row = int(0)
        for url in self.viewUpdate.listData:
            self.setItem( row, 0, TableWidget.getTextColumnItem( url, True ) )
            row += 1

        self.setUpdatesEnabled(True)


    # update the table with values
    def updateTable( self, updateData: ViewUpdate ):
        self.viewUpdate.copy( updateData )
        FunctionPtrTask( "DisplayURLs", self, self.displayUrls )


    # called when our task is done
    def taskComplete( self, task ):
        del task 
        task = None

        
    # updateTable

'''