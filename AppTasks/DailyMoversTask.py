

'''


from AppUI import DailyMoversView
from AppUtils import GuardedList, RequestUrl, HtmlParser
from AppTasks import RepeatingTask
from AppTasks.TaskUtils import FunctionPtrTask


#
# Daily Mover - gainers, losers, most active... 
#
# todo: add others as needed
#


class DailyMoversTask( RepeatingTask ):

    GAINERS_URL = "https://stockanalysis.com/markets/gainers/"
    LOSER_URL   = "https://stockanalysis.com/markets/losers/"
    ACTIVE_URL  = "https://stockanalysis.com/markets/active/"


    def __init__( self, view: DailyMoversView  ):

        RepeatingTask( "DailyWinnersLosersTask", view )

        self._html      = GuardedList()
        self._sleepTime = int(1)

        self.__startTask__()


    def processTask( self ) -> bool:

        urls    = [ self.GAINERS_URL, self.LOSERS_URL, self.ACTIVE_URL ]
        tables  = []

        for url in urls:

            resp = RequestUrl.get( url )
            if resp != None:

                htmlBody = HtmlParser.parseBody( resp )
                tables.append( htmlBody )

        self._parent.updateView( tables )

        return True

'''