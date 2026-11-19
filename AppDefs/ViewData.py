

from enum import Enum

from abc import ABC, abstractmethod

from AppUtils import GuardedDictionary, GuardedDictionaryList


#
# ViewUpdateUsre is used as a callback for table changed data
#
class ViewUser( ABC ):
    
    def __init__(self):
        assert( self )

    @abstractmethod
    def viewDataChanged( self, viewData: ViewData ) -> None:    # type: ignore
        assert( viewData )
        pass
            

#
# View Data - used to update views
#
class ViewData:
    
    def __init__( self, viewType: str, owner: ViewUser ):
 
        self.owner      = owner       
        self.viewType   = viewType
        self.dictData   = GuardedDictionary()
        self.tableData  = GuardedDictionaryList()
    

    def deepCopy( self, other: ViewData ):

        self.owner      = other.owner       
        self.viewType   = other.viewType
        self.dictData   = other.dictData
        self.tableData  = other.tableData

     









        

