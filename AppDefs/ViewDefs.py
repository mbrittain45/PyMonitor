


'''


    # views
    WindowSizes            = []
    WindowMargin           = QRect(8,8,8,8)


   #    
    # compute windows sizes for the entire app now
    #
    @staticmethod
    def computeWindowSizes():
        
        size                = theApp.getWnd.primaryScreen.size()
        left                = size.left()
        top                 = size.top()
        width               = (size.width() - 480)
        height              = (size.height() - 320)
      
        subValue            = int(16)
        while subValue < 513:           # 32 levels is enough
        
            rect            = None
            if left > subValue and top > subValue:
                rect = QRect( left - subValue, top - subValue, width - subValue, height - subValue )
            else:
                rect = QRect( left, top, width - subValue, height - subValue )
            
            Defs.WindowSizes.append( rect )
            subValue      += 16
        

    #
    # get a windows geometry by level where the higher level the smaller the window geometry
    #
    @staticmethod
    def getWindowGeometry( uiLevel: int ):
        
        if Defs.WindowSizes.count() <= 1:
            Defs.computeWindowSizes()

        if uiLevel < 32:
            return Defs.WindowSizes[ uiLevel ]
        return Defs.WindowSizes[ 31 ]
        

    #   
    # get a windows margin buffer, which is the same for everyone currently
    #
    @staticmethod
    def getWindowMargin():
        return Defs.WindowMargin

 


'''
