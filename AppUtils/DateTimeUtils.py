

#import calendar

from datetime import datetime, date, time #, timedelta

#from AppUtils import GuardedDictionary, StrUtils


#
# Epocher - handles getting different format of the beginning of computer time (the epoch)
#
class Epocher:

    @staticmethod
    def getDateTime():
        return datetime( 1970, 1, 1, 0, 0, 0 )

    @staticmethod
    def getDate():
        return date( 1970, 1, 1 )

    @staticmethod
    def getTime():
        return time( 0, 0, 0 )



#
# Date Time Format
#
class DateTimeFmt:
        
    @staticmethod
    def getYear():
        return datetime.now().strftime( "%y" )
   
    # get the 2 digit year
    @staticmethod
    def getTwoDigitYear():
        year = datetime.now().strftime( "%y" )
        return year[ 2 : 3 ]
   
    @staticmethod
    def getMonth():
        return datetime.now().strftime( "%m" )
    
    @staticmethod
    def getMonthYear():
        return datetime.now().strftime( "%m-%y" )
        
    # get the date: month-day-year
    @staticmethod
    def getDate():
        return datetime.now().strftime( "%m-%d-%y" )
    
    # get the time: hours:minutes:seconds
    @staticmethod
    def getTime():
        return datetime.now().strftime( "%H:%M:%S" )

    # get date and time
    @staticmethod 
    def getDateTime():
        return datetime.now().strftime( "%m-%d-%y %H:%M:%S" )



'''


#
# TimestampParser - Date and Timestamp parser for FileNameDTMarker and 
# 
class TimestampParser:

    @staticmethod
    def parseDate( dateStr ):

        tmp      = dateStr 
        m, tmp = StrUtils.getDelimValue( tmp, "-" )
        d, tmp = StrUtils.getDelimValue( tmp, "-" )
        y        = int(tmp)

        return date( int(m), int(d), int(y) )


    # parse the time portion of a file timestamp
    @staticmethod
    def parseTime( timeStr ):

        tmp      = timeStr 
        h, tmp = StrUtils.getDelimValue( tmp, "-" )
        m, tmp = StrUtils.getDelimValue( tmp, "-" )
        s        = tmp

        return time( int(h), int(m), int(s) )



#
# File Name Date Time Marker - we support timestamps appended to file names for time tracking purposes
#
class FileNameTimestamp:

    # get a date time timestamp for appending to a file name in the form:   _month-day-year_hours-minutes-seconds_
    @staticmethod
    def getTimestamp():
        return datetime.now().strftime( "_%m-%d-%y_%H-%M-%S_" )


    # parse the timestamp from a file name in the form:  "_%m-%d-%y_%H-%M-%S_"
    @staticmethod
    def parseTimestamp( filePath ):

        tmp  = filePath

        val, tmp = StrUtils.getDelimValue( tmp, "_" )    # remove leading '_'
        if val == None or tmp == None:
            return Epocher.getDateTime()

        val, tmp = StrUtils.getDelimValue( tmp, "_" )    # get date string
        if val == None or tmp == None:
            return Epocher.getDateTime()
        
        dateStr = val

        val, tmp = StrUtils.getDelimValue( tmp, "_" )    # get time string
        if val == None or tmp == None:
            return Epocher.getDateTime()

        timeStr = val

        return TimestampParser.parseDate( dateStr ), TimestampParser.parseTime( timeStr )



#
# File Date Marker
#
class FileNameDatestamp:

    # get a file date only timestamp: _month-day-year_
    @staticmethod
    def getDatestamp():
        return datetime.now().strftime( "_%m-%d-%y_" )


    # parse a file name date marker, which is at the end of the file name in the form: "_%m-%d-%y.%H-%M-%S_"
    @staticmethod
    def parseDatestamp( filePath ):

        tmp = filePath
        p1  = tmp.find( "_" )
        p2  = tmp.rfind( "_" )
        if p1 != -1 and p2 != -1:           
            TimestampParser.parseDate( tmp[ (p1 + 1) : p2 ] )
        return None, None



#
# InFileTimestmap
#
class FileDelimiterTimestmap:


    # get a timestamp delimiter for use in our files - to make searching quicker
    @staticmethod
    def get( timeValue: None ) -> str:

        if timeValue != None:
            return timeValue.strftime( "<*>%m-%d-%y %H:%M:%S<*>" )
        return datetime.now().strftime( "<*>%m-%d-%y %H:%M:%S<*>" )
    
        
    # parse a file delimiter timestamp in the form: "<*>%m-%d-%y %H:%M:%S<*>"
    @staticmethod
    def parseTimestamp( timestamp ) -> datetime:
    
        tmp = timestamp
        
        tmp.replace( '<*>', '' )

        hour, tmp   = StrUtils.getSubstr( tmp, ":" )
        minute, tmp = StrUtils.getSubstr( tmp, ":" )
        second, tmp = StrUtils.getSubstr( tmp, " " )
        month, tmp  = StrUtils.getSubstr( tmp, "-" )
        day, tmp    = StrUtils.getSubstr( tmp, "-" )
        year        = tmp

        return datetime( int(year), int(month), int(day), int(hour), int(minute), int(second) )        


    # parse a file delimited with timestamps
    @staticmethod
    def parse( text : str ) -> GuardedDictionary:

        retDict = GuardedDictionary()

        tmp = text
        
        # remove leading "<*>"
        empty, tmp = StrUtils.getSubstr( tmp, "<*>" )
        
        # parse the timestamps delimited text file
        while len( tmp ) > 0:

            timestamp, tmp = StrUtils.getSubstr( tmp, "<*>" )

            if tmp.find( "<*>" ) != -1:
                textBlob, tmp = StrUtils.getSubstr( tmp, "<*>" )
            else:
                textBlob = tmp
                tmp.clear()

            retDict[ timestamp ] = textBlob

        return retDict



#
# Date/Time Utility Object
#
class DateTimeUtils:
        
    # get a time delta in milliseconds
    @staticmethod
    def getMsecTimeDelta( timeout: int ):
        return timedelta( milliseconds=timeout )


    # get a time delta in hours
    @staticmethod
    def getHoursTimeDelta( timeout: int ):
        return timedelta( hours=timeout )


    @staticmethod
    def getCurTime():
        datetime.now()
    
    
    # increment the day portion of a date and rollover to months and years as its incremented
    @staticmethod
    def incrementDate( certainDate: datetime ) -> datetime:

        certainDate += timedelta(days=1)
        return certainDate 

        
    # remove the month from a month-year date
    @staticmethod
    def subtractMonthFromMonthYear( myStr ) -> str:
        
        month = int( myStr[ 0 : 2 ] )
        year  = myStr[ 3 : 7 ]
        month = DateTimeUtils.subtractMonth( month )
        return "{}-{}".format( month, year )


    # subract a month
    @staticmethod
    def subtractMonth( month: int ) -> int:

        month -= 1
        if month < 1:
            return 12
        return month


    # add a month
    @staticmethod
    def addMonth( month: int ) -> int:

        month += 1
        if month > 12:
            return 1
        return month


    # get the days in a given month
    @staticmethod
    def getDaysInMonth( month: int, year: int ) -> int:

        # days in each month, zero based w/ position zero being invalid number of days
        DAYS_PER_MONTH = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 
        LEAP_DAYS_PER_MONTH = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 

        if year % 4 == 0:   # leap years
            return int(LEAP_DAYS_PER_MONTH[ month ])
        else:
            return int(DAYS_PER_MONTH[ month ])
               
            
    # get the start date from the number of days in the passed
    @staticmethod
    def getStartDate( numOfDaysBack ) -> date:
        
        year    = int( datetime.now().year )
        month   = int( datetime.now().month )
        day     = int( datetime.now().day )
        
        # subtract years
        while numOfDaysBack > 365:
            if year % 4 == 0:   # leap years
                numOfDaysBack -= 366
            else:
                numOfDaysBack -= 365
            year -= 1
    
        # subtract months
        daysInMonth = DateTimeUtils.getDaysInMonth( month, year )
        while numOfDaysBack > daysInMonth:
            numOfDaysBack   -= daysInMonth
            month           = DateTimeUtils.subtractMonth( month )
            daysInMonth     = DateTimeUtils.getDaysInMonth( month, year )
                    
        # subtract days left
        day -= numOfDaysBack
            
        return date( day, month, year )
    

    # get the week number
    @staticmethod
    def getWeekNumber() -> int:
        
        date_obj = datetime( datetime.now().year, datetime.now().month, datetime.now().day )
        # Get the ISO calendar representation
        iso_calendar_tuple = date_obj.isocalendar()
        # Extract the ISO week number
        return int(iso_calendar_tuple[1])


    # get a number of week numbers from current backwards (week numbers 1-52)
    @staticmethod
    def getWeekNumbers( numWeeks ) -> list[ int ]:

        weekNums    = []
        weekNum     = DateTimeUtils.getWeekNumber()
        weekNums.append( weekNum )
        numWeeks    -= 1
        while numWeeks:
            weekNum   -= 1
            if weekNum <= 0:
                weekNum = 52
            weekNums.append( weekNum )
            numWeeks  -= 1
        return weekNums


    # get time until next month
    @staticmethod
    def getTimeUntilNextMonth():

        year = date.today().year
        if date.today().month == 12:
            year += 1

        endDate = date( year, DateTimeUtils.addMonth( date.today().month), 1 )
        endTime = datetime( endDate.year, endDate.month, endDate.day )

        return endTime - datetime.now()
    

    # get time until next month
    @staticmethod
    def getFirstOfNextMonth():

        year = date.today().year
        if date.today().month == 12:
            year += 1

        now     = datetime.now()
        endDate = date( year, DateTimeUtils.addMonth( date.today().month), 1 )

        return datetime( endDate.year, endDate.month, endDate.day, now.hour, now.minute, now.second )


    # get time until next quarter
    @staticmethod
    def getFirstOfNextQuarter():

        newQuart   = None
        now        = datetime.now()

        if now.month >= 1 and now.month <= 3:
            newQuart = datetime( now.year, int(4), int(1), int(0), int(0), int(0) )
        elif now.month >= 4 and now.month <= 6:
            newQuart = datetime( now.year, int(7), int(1), int(0), int(0), int(0) )
        elif now.month >= 7 and now.month <= 9:
            newQuart = datetime( now.year, int(10), int(1), int(0), int(0), int(0) )
        else:
            newQuart = datetime( (now.year + 1), int(1), int(1), int(0), int(0), int(0) )

        return newQuart


    # get quarter 1-4
    @staticmethod
    def getQuarter():

        now     = datetime.now()
        quart   = (((now.month - 1) / 3) + 1)
        return quart


#
# File Data Time - hold file name. file date and file time
#
class FileDateTime:
    
    def __init__(self, fileName, fileDate, fileTime ) :
        
        self.fileName  = fileName
        self.fileDate  = fileDate
        self.fileTime  = fileTime
        
        
        
        '''