

'''

from UserInterface import eUIEvent
   
from Shared import Dictionary


#
# use the QT UI Event Types to pass around data about specific UI Events
# ie:
#    
# Qt.MouseButton.NoButton	        0 ( 000 )
# Qt.MouseButton.LeftButton	        1 ( 001 )
# Qt.MouseButton.RightButton	    2 ( 010 )
# Qt.MouseButton.MiddleButton    
    
    
#
# Base class for UI Control Parent Objects - so we can state which eUIEvents
#    we are interested in processing. Then get the callback to process those events
#    
class UIParent:
    
    # init
    def __init__( self, parent, uiEvents ): # list[ (eUIEvent, callbackFunc) ] ):
        
        self._procEvents = Dictionary()
        self._parent     = parent
        for e in uiEvents:
            self._procEvents[e] = e


    # see if we are processing a certain eUIEvent
    def isProcessingEvent( self, event: eUIEvent ):
    
        e, f = self._procEvents[ event ]
        
        if e == None and f == None:
            return False
        elif e == None:
            return False
            
        return True
    

    # process a certain eUIEvent
    def processEvent( self, event: eUIEvent ):
        
        e, f = self._procEvents[ event ]
        if e != None:
            f( event )    
            return False
        return True
    

            

  
  
  '''