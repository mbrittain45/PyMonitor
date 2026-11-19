


'''

from threading import threading, Thread

from Application import theApp

from Tasks import ThreadProcessor


#
# Base Thread - our base thread class
#
class BaseThread( Thread ):

    # init
    def __init__( self, name: str, threadProcessor: ThreadProcessor = None ):

        Thread.__init__( self )
        
        self.name              = name
        self._terminateThread  = False
        self._threadTerminated = False
        self._threadProcessor  = None

        if threadProcessor != None:
            self._threadProcessor = threadProcessor
            self._threadProcessor.setBaseThread( self )


    # call to tell us to exit run() and terminate
    def setTerminateThread( self ):

        self._terminateThread = True


    # see if the thread has terminted / is finished
    def hasThreadTerminated( self ):

        return self._threadTerminated

    
    # see if we are alive
    def is_alive( self ) -> bool:

        if self._threadTerminated:
            return False

        return super().is_alive()



    # can be overridden - thread terminates when run() returns
    def run( self ):

        if self._terminateThread:
            self._threadTerminated = True
            return 

        # function must be overridden to perform work if worker object is invalid
        if self._threadWorkerObj == None:
            self.performThreadProcessing()
        else:
            self._threadProcessor.performProcessing()

        self._threadTerminated = True


    # perform the thread processing - this function must be overridden to perform the thread duties
    def performThreadProcessing( self ):
        
        assert( False )

 
'''   