


'''

#
# the Platform Types - we care about linux and windows currently
#
class EPlatformType( Enum ):

    eUnknown    = int(-1)
    eAndroid    = int(0)
    eCocoa      = int(1)
    eDirectfb   = int(2)
    eEglfs      = int(3)
    eIos        = int(4)
    eKms        = int(5)
    eLinuxfb    = int(6)
    eMinimal    = int(7)
    eMinimalegl = int(8)
    eOffscreen  = int(9)
    eOpenwfd    = int(10)
    eQnx        = int(11)
    eWindows    = int(12)
    eWayland    = int(13)
    eXcb        = int(14)



#
# Platform class - defines the OS and Hardware we are running on
#
class Platform:

    # static platform type
    platformType = EPlatformType.eWindows

    def __init__( self ):
        self.platformType = EPlatformType().eUnknown

    def getType( self )-> EPlatformType:
        return self.platformType    


    # set platform type
    @staticmethod
    def setType( name: str ):

        OSNames = [ "android", "cocoa", "direct", "egl", "ios", "kms", "linux", "minimal", "minimal_egl", "offscreen", "openwfd", "qnx", "windows", "wayland", "xcb" ]
        
        i = int(0)
        for osName in OSNames:

            if osName in name:
                Platform.platformType = EPlatformType( i )
                return
            i += 1




'''