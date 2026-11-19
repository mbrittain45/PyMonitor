

'''


from App import theApp, Defs, ViewListUpdate, NewsEntry
from AppTasks.BaseTask import ETaskResult
from AppTasks.TaskUtils import PathChangeHandler, SingleShotTask, FunctionPtrTask
from AppUtils import GuardedList, GuardedDictionary, DirectoryOps, FileOps, TextFile


class GovermentSearchTermsTask:

    INPUT_DIR      = Defs.addToInputDir( "GovernmentSearchTerms" )
    INPUT_FILE     = Defs.makePath( INPUT_DIR, "GovernmentSearchTerms.txt" )

    # init 
    def __init__( self ):

        DirectoryOps.createDir( self.INPUT_DIR )
        self._searchTerms = GuardedList()
        self.readGovernmentSearchTerms()
        

    # get field names for our view
    def getFieldNames(self) -> list[str]:
        return [ "Government Search Strings" ] 


    # get the mist search terms
    def getSearchTerms( self ):
        return self._searchTerms.getList()


    # callback function when a file changes
    def fileChanged( self, fileName ):

        if fileName == self.INPUT_FILE:
            FunctionPtrTask( "ReadGovernmentSearchTerms", self, self.readGovernmentSearchTerms )
        else:
            assert( False )


    # read our search strings 
    def readGovernmentSearchTerms( self ):

        if FileOps.doesFileExists( self.INPUT_FILE ):

            searchStrings = TextFile.read( self.INPUT_FILE, True )
            if searchStrings.count() > 0:
                
                self._searchTerms.copyList( searchStrings )
                theApp.getTaskMgr().updateView( ViewListUpdate( Defs.EViewType.eGovernmentSearchTerms, self._searchTerms.getList() ) )
                theApp.setMiscSearchTerms( self._searchTerms.getList() )
        else:
            FileOps.createFile( self.INPUT_FILE )
    
        if not theApp.getFileMonitor().isMonitored( self.INPUT_FILE ):
            theApp.getFileMonitor().addPath( self.INPUT_FILE, self )

                
    # clean up our function task
    def taskComplete( self, task ):
        del task
        task = None




'''