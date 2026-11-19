



'''

from PySide6.QtWidgets import QStatusBar, QListWidget


#
# Stock Status Bar
#
class StatusBar( QStatusBar ):


    # init object
    def __init__(self):
        super().__init__(self)

        self.setTitle( "Alerts and Errors" )
        self._rows = int(0)

        self.setGeometry( 25, 25, 100, 1500 )
        self.setContentsMargins( 5, 10, 5, 10 )
                       
        self.listWidget = QListWidget()
        self.listWidget.setGeometry( 20, 20, 90, 1250 )
        self.listWidget.setContentsMargins( 5, 5, 5, 5 )
        self.listWidget.setSortingEnabled( False )

        self.setWidget( self.listWidget )


    # remove the last 10 rows
    def __removeRows__(self):

        self._rows -= 1
        while self.rows > 35:
            self.listWidget.takeItem( self.rows )
            self._rows -= 1


    # count a new row added
    def __newRowAdded__( self ):
        
        self._rows += 1
        if self._rows > 50:
            self.__removeRows__()
    

    # todo: customize w/ icon types and coloring

    # add item to head of list widget
    def addNewError( self, text ):

        self.listWidget.insertItem( 0, text )
        self.__newRowAdded__()

        

    # add item to head of list widget
    def addNewAlert( self, text ):

        self.listWidget.insertItem( 0, text )
        self.__newRowAdded__()
       

   
   
   
   '''