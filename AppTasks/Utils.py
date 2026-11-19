
'''

from Application import theApp

from Shared import TimeUtils


#
# SQL Trace Utility
#
class SQLTrace:

    @staticmethod
    def op( msg: str ):
        theApp.getLogger().logInfo( msg )
        theApp.sqlWnd().display( msg )



'''