

# pylint: disable=no-name-in-module
from PySide6.QtCore import QMutexLocker, QWaitCondition, QRecursiveMutex

from typing import Any

from enum import Enum

#
# NamedMutex - can only be shared inside the application
#
class NamedMutex( QRecursiveMutex ):
    
    def __init__(self, name: str):
        QRecursiveMutex.__init__(self)
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
        self._mutex = QRecursiveMutex()


#
# Guarded Queue - built on a list w/ a mutex
#
class GuardedQueue( BaseGuard ):

    def __init__(self):

        BaseGuard.__init__(self)
        self._queue = [Any]
        

    def popHead( self ) -> Any:

        with QMutexLocker( self._mutex ):
            return self._queue.pop(0)


    def addTail( self, val: Any ) -> None: 

        with QMutexLocker( self._mutex ):
            self._queue.append( val )  


    def getCount(self) -> int:
 
       with QMutexLocker( self._mutex ):
            return len(self._queue)


    def appendList( self, values: list[Any] ) -> None:

       with QMutexLocker( self._mutex ):
            for val in values:
                self._queue.append( val )  
            
    
    def getList( self ) -> list[Any]:

        rlist: list[Any] = []
        with QMutexLocker( self._mutex ):
            for val in self._queue:
                rlist.append( val )  
            return rlist




    
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

    
    def getKeys(self) -> list[Any]:

        with QMutexLocker( self._mutex ):
            return self._dictionary.keys()      # type: ignore


    def getDict(self) -> dict[Any, Any]:  

        with QMutexLocker( self._mutex ):
            return self._dictionary             # type: ignore


    def copyDict(self, newDict: dict[ Any, Any ] ) -> None:
        
        with QMutexLocker( self._mutex ):
        
            keys = newDict.keys()               # type: ignore
            for key in keys:                    # type: ignore
                self._dictionary[key] = newDict[key]        # type: ignore


    def copyList(self, copyList: list[Any] ) -> None:

        with QMutexLocker( self._mutex ):

            for val in copyList:                # type: ignore
                self._dictionary[val] = val     # type: ignore


    def getCopy(self) -> dict[ Any, Any ]:
        
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
        
        
    def getItem( self, pos: int ) -> Any:            
        
        with QMutexLocker( self._mutex ):
        
            return self._list[ pos ]            # type: ignore
        
        
    def addItem( self, item: Any ) -> None:
           
        with QMutexLocker( self._mutex ):

            self._list.append( item )           # type: ignore
    

    def insertItem( self, pos: int, item: Any ) -> None:

        with QMutexLocker( self._mutex ):

            self._list.insert( pos, item )      # type: ignore
    

    def popHead( self ) -> Any:

        with QMutexLocker( self._mutex ):

            return self._list.pop( 0 )          # type: ignore
    

    def popItem(self, pos: int ) -> Any:          

        with QMutexLocker( self._mutex ):

            if pos >= 0 and pos < self.getCount():
                return self._list.pop( pos )    # type: ignore
            return None 
            
    
    def getCount(self) -> int:                  

        with QMutexLocker( self._mutex ):
            return self._list.count()           # type: ignore
    

    def copyList( self ) -> list[Any]: 

        with QMutexLocker( self._mutex ):
            
            newList = self._list.copy()         # type: ignore
            return newList                      # type: ignore


    def clearList( self ) -> None:

        with QMutexLocker( self._mutex ):

            self._list.clear()                  # type: ignore


    def appendList( self, newList: list[Any] ) -> None:

        with QMutexLocker( self._mutex ):
            
            for val in newList:
                self._list.append( val )        # type: ignore



#
# Guarded Dictionary List (key to values dictionary)
#
class GuardedDictionaryList( BaseGuard ):


    def __init__(self):

        BaseGuard.__init__(self)
        self._dictionary: dict[Any, list[Any] ] = { } 
      
    def clear( self ) -> None:

        with QMutexLocker( self._mutex ):
            self._dictionary.clear()           
        
    def getItems( self, key: Any ) -> list[Any]:
        
        with QMutexLocker( self._mutex ):
            return self._dictionary[ key ]      # type: ignore


    def addItems( self, key: Any, values: list[Any] ) -> None:  

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None:     # type: ignore

                self._dictionary[ key ] = values    # type: ignore
            
            else:
            
                for val in values:
                    self._dictionary[ key ].append( val )   # type: ignore
                

    def addItem( self, key: Any, value: Any ) -> None: 

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None: # type: ignore
                self._dictionary[ key ] = []    # type: ignore
            
            self._dictionary[ key ].append( value ) # type: ignore


    def popItems(self, key: Any) -> list[Any]:

        with QMutexLocker( self._mutex ):

            return self._dictionary.pop( key )  # type: ignore


    def getKeys(self) -> list[Any]:

        with QMutexLocker( self._mutex ):

            return self._dictionary.keys()      # type: ignore

    
    def hasKey( self, key: Any ) -> bool:

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ] == None: # type: ignore
                return False

            return True 


    def removeItem( self, key: Any, value: Any ) -> None:

        with QMutexLocker( self._mutex ):

            if self._dictionary[ key ].count() == 1:        # type: ignore
                self._dictionary.pop( key )                 # type: ignore
            else:
                self._dictionary[ key ].remove( value )     # type: ignore
           

    def removeKey( self, key: Any ) -> None:

        with QMutexLocker( self._mutex ):
            self._dictionary.pop( key )                     # type: ignore


    def copy( self, gdict: GuardedDictionaryList ):

        with QMutexLocker( self._mutex ):
        
            keys = gdict.getKeys()
            for key in keys:

                items = gdict.getItems( key )

                self._dictionary[ key ] = []    # type: ignore

                for item in items:
                    self._dictionary[ key ].append( item ) # type: ignore


    def tableDataChanged( self, row: int, column: int, value: str ) -> None:

        with QMutexLocker( self._mutex ):

            irow = 0        

            keys = self.getKeys()
            for key in keys:

                if row == irow:
                
                    items = self.getItems( key )
                    items[ column ] = value
                    self._dictionary[ key ] = items # type: ignore      
                    return
                
                irow += 1

        


#
# GuardedSet we use a dictionary that only holds key values
#
# set functions:
#
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
#            	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#            	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
#
class GuardedSet( BaseGuard ):


    def __init__(self):
        
        BaseGuard.__init__(self)
        self.set = set()  # type: ignore
        
        
    def hasItem( self, key: Any ) -> bool:

        with QMutexLocker( self._mutex ):

            if key in self.set: # type: ignore
                return True
            return False


    def addItem( self, key: Any ): 
        
        with QMutexLocker( self._mutex ):
            self.set.add( key ) # type: ignore


    def popItem(self, key: Any) -> Any:        

        with QMutexLocker( self._mutex ):
            return self.set.pop( key )          # type: ignore

    
    def getSet(self) -> set(Any): # type: ignore

        with QMutexLocker( self._mutex ):
            return self.set    # type: ignore


    def removeItem( self, key: Any ) -> None:
    
        with QMutexLocker( self._mutex ):
            return self.set.remove( key )       # type: ignore


    def getLen( self ) -> int:

        return len( self.set )      # type: ignore





class GuardedMultiKeyDict( BaseGuard ):

    class EKeyType( Enum ):
        
        eMainKey    = int(0),      # the main lookup key
        eXref1Key   = int(1),      # an aux1 key
        eXref2Key   = int(2)       # an aux2 key


    def __getMainItem__( self, key: Any ) -> Any:

        return self.mainDict[ key ] # type: ignore
                 
        

    def __init__(self):

        BaseGuard.__init__(self)

        self.mainDict  = dict()   # type: ignore
        self.xref1Dict = dict()   # type: ignore
        self.xref2Dict = dict()   # type: ignore

        
    # has an item
    def hasItem( self, key: Any, keyType: EKeyType ) -> bool:

        with QMutexLocker( self._mutex ):

            if keyType == self.EKeyType.eMainKey:
                if self.mainDict[ key ] == None:    # type: ignore
                    return False
            
            if keyType == self.EKeyType.eXref1Key:
                if self.xref1Dict[ key ] == None:   # type: ignore
                    return False
            
            if keyType == self.EKeyType.eXref2Key:
                if self.xref2Dict[ key ] == None:   # type: ignore
                    return False
            
            return True


    # get an item by key and key type
    def getItem( self, key: Any, keyType: EKeyType ) -> Any:

        with QMutexLocker( self._mutex ):

            if keyType == self.EKeyType.eMainKey:
                return self.__getMainItem__( key )
            
            if keyType == self.EKeyType.eXref1Key:

                mainKey = self.xref1Dict[ key ]     # type: ignore
                if mainKey != None:                 # type: ignore
                    return self.__getMainItem__( mainKey )
            
            if keyType == self.EKeyType.eXref2Key:

                mainKey = self.xref2Dict[ key ]     # type: ignore
                if mainKey != None:                 # type: ignore
                    return self.__getMainItem__( mainKey )

            assert( False )
            return None      # type: ignore


    # add an item and keys
    def addItem( self, value: Any, mainkey: Any, aux1Key: Any = "", aux2Key: Any = ""  ): 
        
        with QMutexLocker( self._mutex ):

            self.mainDict[ mainkey ] = value                # type: ignore

            if len( aux1Key ) > 0:
                self.xref1Dict[ aux1Key ] = mainkey         # type: ignore

            if len( aux2Key ) > 0:
                self.xref2Dict[ aux2Key ] = mainkey         # type: ignore


    # add an alias
    def addAlias( self, mainkey: Any, aux1Key: Any ): 
        
        with QMutexLocker( self._mutex ):

            if self.hasItem( mainkey, self.EKeyType.eMainKey ):
                self.xref1Dict[ aux1Key ] = mainkey         # type: ignore
            else:
                assert( False )
            

    # add aliases
    def addAliases( self, mainkey: Any, aux1Key: Any, aux2Key: Any ): 
        
        with QMutexLocker( self._mutex ):

            if self.hasItem( mainkey, self.EKeyType.eMainKey ):
                self.xref1Dict[ aux1Key ] = mainkey         # type: ignore
                self.xref2Dict[ aux2Key ] = mainkey         # type: ignore
            else:
                assert( False )
            

    # get keys by key type
    def getKeys(self, keyType: EKeyType ) -> list[Any]:

        with QMutexLocker( self._mutex ):

            if keyType == self.EKeyType.eMainKey:
                return self.mainDict.keys()         # type: ignore
            
            if keyType == self.EKeyType.eXref1Key:
                return self.xref1Dict.keys()        # type: ignore
            
            if keyType == self.EKeyType.eXref2Key:
                return self.xref2Dict.keys()        # type: ignore

            return self.mainDict.keys()             # type: ignore






'''    
    def __getDataMap__( self, valList: list[Any]  ) -> dict{str, Any}:       # type: ignore

            index = int(0)
            data = { "Len": len(valList) }
   
            for val in valList:
                data.update( { f"{index}": val } )
                index += int(1)
                
            return data


    # serialize to a file
    def serializeToFile( self, filePath: str ):

        mainKeys  = self.mainDict.keys()  # type: ignore
        xref1Keys = self.xref1Dict.keys() # type: ignore
        xref2Keys = self.xref2Dict.keys() # type: ignore

        data = {
            'mainKeysLen': len(mainKeys),       # type: ignore
            'xref1KeysLen': len(xref1Keys),      # type: ignore
            'xref2KeysLen': len(xref2Keys),        # type: ignore
            'mainMapKeys': self.__getDataMap__( mainKeys ),      # type: ignore
            'mainMapVals': self.__getDataMap__( self.mainDict.values() ),      # type: ignore
            'xref1MapKeys': self.__getDataMap__( xref1Keys ),      # type: ignore
            'xref1MapVals': self.__getDataMap__( self.xref1Dict.values() ),      # type: ignore
            'xref2MapKeys': self.__getDataMap__( xref1Keys ),      # type: ignore
            'xref2MapVals': self.__getDataMap__( self.xref1Dict.values() )      # type: ignore
        }

        with open( filePath, 'wb' ) as file:
            pickle.dump( data, file )





    def popItem(self, key: Any) -> Any:        

        with QMutexLocker( self._mutex ):
            return self._dictionary.pop( key )  # type: ignore

    
    def getKeys(self) -> list[Any]:

        with QMutexLocker( self._mutex ):
            return self._dictionary.keys()      # type: ignore

'''