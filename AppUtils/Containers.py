

# pylint: disable=no-name-in-module
from PySide6.QtCore import QMutexLocker, QMutex, QWaitCondition

from typing import Any



#
# NamedMutex - can only be shared inside the application
#
class NamedMutex( QMutex ):
    
    def __init__(self, name: str):
        QMutex.__init__(self)
        self._name  = name
    
    def getName(self):
        return self._name


    
#
# Wait Condition - wait on a mutex
#
class WaitCondition( QWaitCondition ):

    def __init__( self ):
        QWaitCondition.__init__( self )
        


#
# BaseGuard - holds a mutex for guarded containers
#
class BaseGuard:

    def __init__(self):
        self._mutex = QMutex()


#
# Guarded Queue - built on a list w/ a mutex
#
class GuardedQueue( BaseGuard ):

    def __init__(self):
        BaseGuard.__init__(self)
        self._queue = [Any]
        

    def getHead( self ) -> Any:
        with QMutexLocker( self._mutex ):
            return self._queue.pop(0)


    def addItem( self, val: Any ) -> None: 
        with QMutexLocker( self._mutex ):
            self._queue.append( val )  


    def getCount(self) -> int:
 
       with QMutexLocker( self._mutex ):
            return len(self._queue)


    
#
# Guarded Dictionary - Dictionary
# Methods: 
#   clear()         - Removes all items from the dictionary
#   copy()          - Returns a shallow copy of the dictionary
#   fromkeys()      - Creates a dictionary from the given sequence
#   get()           - Returns the value for the given key
#   items()         - Return the list with all dictionary keys with values
#   keys()          - Returns a view object that displays a list of all the keys in the dictionary in order of insertion
#   pop()           - Returns and removes the element with the given key
#   popitem()       - Returns and removes the item that was last inserted into the dictionary.
#   setdefault()    - Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
#   values()        - Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently
#   update()        - Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. With this method, you can include new data or merge it with existing dictionary entries
#
class GuardedDictionary( BaseGuard ):


    def __init__(self):
        BaseGuard.__init__(self)
        self._dictionary = dict()   # type: ignore
        
        
    def hasItem( self, key: Any ) -> bool:

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None: # type: ignore
                return False
            return True


    def getItem( self, key: Any ) -> Any:

        with QMutexLocker( self._mutex ):
            return self._dictionary[ key ]      # type: ignore


    def addItem( self, key: Any, value: Any ): 
        
        with QMutexLocker( self._mutex ):
            self._dictionary[ key ] = value     # type: ignore


    def popItem(self, key: Any) -> Any:        

        with QMutexLocker( self._mutex ):
            return self._dictionary.pop( key )  # type: ignore

    
    def getKeys(self) -> list(Any):             # type: ignore

        with QMutexLocker( self._mutex ):
            return self._dictionary.keys()      # type: ignore


    def getDict(self) -> dict[Any, Any]:  

        with QMutexLocker( self._mutex ):
            return self._dictionary             # type: ignore


    def copyDict(self, newDict: dict[ Any, Any ] ) -> None:  # type: ignore
        
        with QMutexLocker( self._mutex ):
        
            keys = newDict.keys()               # type: ignore
            for key in keys:                    # type: ignore
                self._dictionary[key] = newDict[key]        # type: ignore


    def copyList(self, copyList: list[any] ) -> None:  # type: ignore

        with QMutexLocker( self._mutex ):

            for val in copyList:                # type: ignore
                self._dictionary[val] = val     # type: ignore


    def getCopy(self) -> dict:                  # type: ignore
        
        retDict = dict()                        # type: ignore
        
        with QMutexLocker( self._mutex ):

            keys = self._dictionary.keys()      # type: ignore
            
            for key in keys:                    # type: ignore
                retDict[ key ] = self._dictionary[ key ]  # type: ignore

        return retDict                          # type: ignore




#
# Guarded List
#
class GuardedList( BaseGuard ):


    def __init__(self):
        BaseGuard.__init__(self)
        self._list    = []
        
        
    def getItem( self, pos: int ):              # type: ignore
        
        with QMutexLocker( self._mutex ):
        
            return self._list[ pos ]            # type: ignore
        
        
    def addItem( self, item: Any ):
        
        with QMutexLocker( self._mutex ):

            self._list.append( item )           # type: ignore
    

    def insertItem( self, pos: int, item: Any ):

        with QMutexLocker( self._mutex ):

            self._list.insert( pos, item )      # type: ignore
    

    def popHead( self ):                        # type: ignore

        with QMutexLocker( self._mutex ):

            return self._list.pop( 0 )          # type: ignore
    

    def popItem(self, pos: int ):               # type: ignore

        with QMutexLocker( self._mutex ):

            return self._list.pop( pos )        # type: ignore
    

    def getCount(self) -> int:                  # type: ignore

        with QMutexLocker( self._mutex ):

            return self._list.count()           # type: ignore
    

    def getList(self) -> list[Any]:

        with QMutexLocker( self._mutex ):

            return self._list                   # type: ignore
    

    def copyList( self, otherList: list[Any] ) -> None: 

        with QMutexLocker( self._mutex ):

            self._list.copy( otherList )        # type: ignore


    def clearList( self ) -> None:

        with QMutexLocker( self._mutex ):

            self._list.clear()                  # type: ignore


    def appendList( self, newList: list[Any] ): # type: ignore

        with QMutexLocker( self._mutex ):
            
            for val in newList:

                self._list.append( val )        # type: ignore



#
# Guarded Dictionary List (key to values dictionary)
#
class GuardedDictionaryList( BaseGuard ):


    def __init__(self):
        BaseGuard.__init__(self)
        self._dictionary = dict()               # type: ignore
        

    def getItems( self, key: Any ):             # type: ignore
        with QMutexLocker( self._mutex ):
            return self._dictionary[ key ]      # type: ignore


    def addItems( self, key: Any, values: list[Any] ):  

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None:     # type: ignore

                self._dictionary[ key ] = values    # type: ignore
            
            else:
            
                for val in values:
                    self._dictionary[ key ].append( val )   # type: ignore
                

    def addItem( self, key: any, value: any ):  # type: ignore

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None: # type: ignore
                
                self._dictionary[ key ] = []    # type: ignore
            
            self._dictionary[ key ].append( value ) # type: ignore


    def popItems(self, key: any):               # type: ignore

        with QMutexLocker( self._mutex ):

            return self._dictionary.pop( key )  # type: ignore


    def getKeys(self):                          # type: ignore

        with QMutexLocker( self._mutex ):

            return self._dictionary.keys()      # type: ignore

    
    def hasKey( self, key: Any ):               # type: ignore

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None: # type: ignore
                return False

            return True 

            
