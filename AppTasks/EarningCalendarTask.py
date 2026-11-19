
'''


from App import theApp, Defs, ViewListUpdate
from AppTasks.BaseTask import ETaskResult
from AppTasks.TaskUtils import SingleShotTask
from AppUtils import FileOps, RequestUrl, TextFile, GuardedDictionaryList


#
# Earning Calendar Task - get the earnings calendar for the next few weeks.
#       We should only run once a day to check on the calendar.
#
class EarningsCalendarTask( SingleShotTask ):
    
    OUTPUT_DIR      = Defs.addToCacheDir( "EarningsData" )
    OUTPUT_FILE     = Defs.makePath( OUTPUT_DIR, "EarningsData" + Defs.DATA_EXT )
    
    DUMP_FILE       = Defs.makePath( OUTPUT_DIR, "EarningsDumpData" + Defs.DATA_EXT )

    URL             = "https://stockanalysis.com/stocks/earnings-calendar/"


    def __init__(self, parent):

        SingleShotTask.__init__( self, "EarningsCalendarTask", parent )

        companies = GuardedDictionaryList()
        if FileOps.doesFileExist( self.OUTPUT_FILE ):
            self.readOutputFile()


    def processTask(self) -> bool:

        resp = RequestUrl.get( self.URL )
        if resp != None:

            TextFile.queueWriteFile( self.DUMP_FILE, resp, False ) 

            # todo: figure how to parse and select the various days..
            #self.parseEarningsTable( resp )

        return True


'''