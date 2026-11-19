

from AppDefs import Security

from AppUtils import GuardedMultiKeyDict, GuardedDictionary



#
# App Securities - holds all stock and etfs
#
class AppSecurities():

#    SECURITIES_FILE  = DirDefs.addToOutputDir( "Securities.dat" ) 
#    SECURITIES_STATS = DirDefs.addToOutputDir( "SecurityStats_{}.dat" ) 
 
    Securities       = GuardedMultiKeyDict()


    @staticmethod
    def setStocks( securities: GuardedDictionary ) -> None:
        
        securityKeys = securities.getKeys()
        for securityKey in securityKeys:
            
            stock: Security = securities.getItem( securityKey )
            AppSecurities.Securities.addItem( stock, stock.name, stock.symbol, stock.uid ) 


    @staticmethod
    def findSecurityByName( name: str ) -> Security:
        return AppSecurities.Securities.getItem( name, GuardedMultiKeyDict.EKeyType.eMainKey )


    @staticmethod
    def findSecurityBySymbol( symbol: str ) -> Security:
        return AppSecurities.Securities.getItem( symbol, GuardedMultiKeyDict.EKeyType.eXref1Key )


    @staticmethod
    def findSecurityByUid( uid: int ) -> Security:
        return AppSecurities.Securities.getItem( uid, GuardedMultiKeyDict.EKeyType.eXref2Key )


    @staticmethod
    def getCompanyNames() -> list[str]:
        return AppSecurities.Securities.getKeys( GuardedMultiKeyDict.EKeyType.eMainKey )


    @staticmethod
    def getStockSymbols() -> list[str]:
        return AppSecurities.Securities.getKeys( GuardedMultiKeyDict.EKeyType.eXref1Key )


'''

    todo: who writes stock statistics and how often do we get them

    @staticmethod
    def writeStatsFile():
        # todo:
        assert( False )


    @staticmethod
    def readStatsFiles():
        # todo:
        assert( False )


    @staticmethod
    def writeSecuritiesFile():

        blob     = ""
        mainKeys = AppSecurities.Securities.getKeys( GuardedMultiKeyDict.EKeyType.eMainKey )

        for key in mainKeys:
            security = AppSecurities.Securities.getItem( key, GuardedMultiKeyDict.EKeyType.eMainKey )
            if security:
                blob += security.toFileFmt()

        FileOperation.createWriteBlobFileOp( AppSecurities.SECURITIES_FILE, blob, None, False ) # type: ignore


    @staticmethod
    def readSecuritiesFile():

        FileOperation.createReadBlobFileOp( AppSecurities.SECURITIES_FILE, None, False ) # type: ignore


    @staticmethod
    def processReadSecuritiesFile( fileOp: FileOperation ):
    
        blob = fileOp.data.blob                     # type: ignore
        while len( blob ) > 0:                      # type: ignore

            security = Security()
            
            blob = security.fromFileFmt( blob )     # type: ignore
            
            AppSecurities.Securities.addItem( security, security.name, security.symbol, security.uid )



    # function must be implemented by derived class
    def fileOpComplete(self, fileOp: FileOperation ) -> None:

        if fileOp.handleError():
            return

        if fileOp.type == EFileOpType.eRead and fileOp.filepath == AppSecurities.SECURITIES_FILE:
            AppSecurities.processReadSecuritiesFile( fileOp )

        del fileOp

'''