

from AppUtils import GuardedList
from AppBaseTask import RepeatingTask
from AppUI import GenericPage
from App import theStockApp
from AppServices import AppAbbrvApi

#
# we update all the generic page tabs via the GenericPage.gUpdateQueue, which is global and used for all displayed pages
#
class PageUpdateTask( RepeatingTask ):

           
    def __init__( self ):

        RepeatingTask.__init__( self, "PageUpdaterTask", theStockApp.getTaskMgr() )
        self.sleepTimeout = .25
        self.__startTask__()


    @staticmethod
    def getPage( pageName: str ) -> GenericPage:  
        return AppAbbrvApi.getMainWnd().pages.getItem( pageName )
    

    @staticmethod
    def getPageNames() -> list[str]:
        return AppAbbrvApi.getMainWnd().pages.getKeys()


    # processthe generic table global update queue, which all generic pages share.            
    def processTask( self ) -> bool:  

        updateKeys = GenericPage.gUpdateQueue.getKeys()
        for pageName in updateKeys:

            page = self.getPage( pageName )  # get the specific page by name
            if page:

                glist = GuardedList()
                glist.appendList( GenericPage.gUpdateQueue.popItems( pageName ) )

                cnt = 0
                while cnt < glist.getCount():
                    rowitems = glist.getItem( cnt )
                    page.updateSingleRow( page.windowTitle(), rowitems )   
                    cnt += 1

        return True           
        

