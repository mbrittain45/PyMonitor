



from AppUtils import TimeInsensitiveRequestUrl

from FileSystem import FileOpParent, FileOperation

from AppDefs import DirDefs


class TestRequest( FileOpParent ):


    def __init__( self, url: str ):

        resp = TimeInsensitiveRequestUrl.requestAndSave( url, DirDefs.addToDataDir( f"TestRequest_{url}.txt" ), self )
        if resp[0]:
            rsp = resp[1]
            print( rsp.text )


    def fileOpComplete(self, fileOp: FileOperation ) -> None:

        print( "Request Finished" )
