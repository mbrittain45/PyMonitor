

from enum import Enum
from typing import Any

# pylint: disable=no-name-in-module
from PySide6.QtCore import QTimer, QObject

from abc import ABC, abstractmethod


#
# Abstract Timer User - users of Timers must derive from this class
# so that the timer can easily call you back when the timer elapses.
#
class AbstractTimerUser(ABC):

    @abstractmethod
    def timerCallback(self) -> None:
        pass



#
# a True One Shot Timer - can only be used repeated but start needs to be called each time 
#
class OneShotTimer( QObject ):

    def __init__( self, user: AbstractTimerUser ):

        self.user = user;


    def timercallback( self ):

        self.user.timerCallback()
       

    def startSingleShot( self, sleepTime: int ) -> None :

        QTimer.singleShot( sleepTime, self, self.timercallback )



#
# Timeout Measurement type      
#
class ETimeoutType( Enum ):

    eMinutes   = int(0)     # minutes
    eSeconds   = int(1)     # seconds
    eMillisecs = int(2)     # milliseconds
    eMicrosecs = int(3)     # microseconds


#
# RepeatingTimer - a repeating timer that calls back the timer user every time the timeout interval elapses.
#
class RepeatingTimer( QTimer ):
    
    MINS_TO_MSECS   = int(60000)
    SECS_TO_MSECS   = int(1000)
    MSECS_TO_USECS  = int(1000)

    
    # init the timer
    def __init__( self, sleepTime: int, user: AbstractTimerUser, timeoutType: ETimeoutType = ETimeoutType.eMinutes ):
        
        QTimer.__init__( self )

        self.timerUser = user
        
        timeout = int(sleepTime)

        if timeoutType == ETimeoutType.eMinutes:
            timeout = int( sleepTime * self.MINS_TO_MSECS )
        elif timeoutType == ETimeoutType.eSeconds:
            timeout = int( sleepTime * self.SECS_TO_MSECS )
        else:
            timeout = int( sleepTime / self.MSECS_TO_USECS )
   
        self.connect( self, QTimer.timeout, self, self.timercallback )  # type: ignore # connect the callback function
        
        self.start( timeout )   # start the timer in msecs


    def timercallback( self ):
  
        self.timerUser.timerCallback() # type: ignore



#
# Timed Value - starts a timer once the value changes from the initial/reset value then
# when the timer elapses the value is reset to the reset/initial value.
#                  
class TimedResetValue( AbstractTimerUser ):
    

    def __init__( self, initialValue: Any, duration: float, timeoutType: ETimeoutType = ETimeoutType.eMillisecs ):
    
        self.timedValue     = initialValue
        self.resetValue     = initialValue
        self.duration       = duration

        if timeoutType == ETimeoutType.eMinutes:
            self.duration   = int(duration * RepeatingTimer.MINS_TO_MSECS)
        elif timeoutType == ETimeoutType.eSeconds:
            self.duration   = int(duration * RepeatingTimer.SECS_TO_MSECS)
        elif timeoutType == ETimeoutType.eMicrosecs:
            self.duration   = int(duration / RepeatingTimer.MSECS_TO_USECS)

        self.timer          = None
        


    def timerCallback(self) -> None:

        self.timedValue = self.resetValue
        self.timer = None

        
    def setValue(self, value: Any ):
        
        self.timedValue = value

        if self.timedValue != self.resetValue and self.timer == None:
        
            self.timer = OneShotTimer( self )
            self.timer.startSingleShot( int(self.duration) )
        

    def getValue(self):

        return self.timedValue
    

