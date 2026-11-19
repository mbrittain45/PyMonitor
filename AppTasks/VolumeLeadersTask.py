

'''

from AppTasks.BaseTask import ETaskResult
from AppTasks import RepeatingTask, FunctionPtrTask
from AppTasks.TaskUtils import PathChangeHandler
from AppUtils import RequestUrl, HtmlParser, Log, GuardedList, GuardedDictionary, TextFile



#
# Daily Active Volume Leaders Task - download only while our view is active
#
class VolumeLeadersTask( RepeatingTask ):

    URL = "https://www.barchart.com/stocks/most-active/daily-volume-leaders?viewName=main&orderBy=volume&orderDir=desc"

    # init
    def __init__( self, activeView ):

        RepeatingTask.__init__( "VolumeLeadersTask", activeView )
        self.sleepTime = int(2)
        self.__startTask__()


    # our processing task thread function
    def processTask( self ) -> bool:
    
        try:

            resp = RequestUrl.get( self.URL )
            if resp != None:
        
                htmlTable = HtmlParser.parseTableBody( resp )
                self.parent.updateView( htmlTable )

                TextFile.queueWriteFile( "VolumeLeadersTaskDump.txt", False )

            else:
                Log.error( ("Unable to get Response for URL: " + self.URL) )
                return False
        
        except:

            Log.error( ("DailyActiveVolumeLeadersTask.processTask - Exception while processing URL: " + self.URL) )
            return False
            
        return True


'''