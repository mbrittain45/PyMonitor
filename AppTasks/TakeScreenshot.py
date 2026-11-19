

'''

import pyautogui
import pygetwindow

from Shared import FileOps, StrDefs

#
# define a Window Region [x, y, width, height]
#
class WndRegion:

    def __init__( self, x: int, y: int, width: int, height: int ):

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height



# 
# To take a screenshot from a Python application, you can use the pyautogui library, 
# which provides a simple function called screenshot() to capture the entire screen
# or a specific region; you can then save the captured image to a file as needed. 
#
class Screenshot:


    # get an apps window region
    @staticmethod
    def getAppWindowREgion( self, appName: str ) -> WndRegion:

        window_title = appName #"Name of the window"

        try:
        
            window = pygetwindow.getWindowsWithTitle( window_title )[0]
        
            if window:
                return WndRegion( window.left, window.top, window.width, window.height )
        
        except IndexError:
            assert( False ) # todo: log error

        return None





    # capture a full screen screenshot    
    @staticmethod
    def captureFullScreen( self, saveImagePath: str, saveImageName: str ):

        screenshot = pyautogui.screenshot()

        FileOps.createDir( saveImagePath )
        screenshot.save( (saveImagePath + StrDefs.DIR_SEP + saveImageName) )
        
        del screenshot



    # capture a specific region
    @staticmethod
    def catpureRegion( self, wndRegion: WndRegion, saveImagePath: str, saveImageName: str ):

        screenshot = pyautogui.screenshot( region=( wndRegion.x, wndRegion.y, wndRegion.width, wndRegion.height ) )

        FileOps.createDir( saveImagePath )
        screenshot.save( (saveImagePath + StrDefs.DIR_SEP + saveImageName) )
        
        del screenshot


'''