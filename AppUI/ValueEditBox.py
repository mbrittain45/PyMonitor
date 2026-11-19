


'''

from PySide6.QtCore import Slot

from PySide6.QtGui import QWindow

from PySide6.QtWidgets import QPushButton, QLineEdit, QMessageBox

from Application import theCfg, theApp


#
# Value Edit Box Parent base class
#
class ValueEditBoxParent:

    def setValueEditBoxComplete( self, text: str ):
        self.getClient().display( "ValueEditBoxParent.setComplete must be overridden. Text Value Entered: {}".format( text ) )
        assert( False )    
        



#
#
# Value Edit Box
#
class ValueEditBox(QWindow):

    def __init__( self, uiLevel: int, parent: ValueEditBoxParent, text: str ):
        
        super().__init__()
        
        self._parent = parent
        self._text   = text
        
        self.setWindowTitle( "Value Edit Box" )
        self.setGeometry( theCfg.getWindowGeometry( uiLevel )  )
        self.initUI()
        
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.setText( self._text )
        
        self.button = QPushButton('Display Text', self)
        self.button.move(20,80)
        
        self.button.clicked.connect(self.onClick)
        

    @Slot()
    def onClick(self):
        
        ret = QMessageBox.question( self, "Value Edited:", self.textbox.text(), (QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Close) )
        if ret == QMessageBox.Ok:
            self._parent.setValueEditBoxComplete( self.textbox.text() )
        elif ret == QMessageBox.Close:
            self._parent.setValueEditBoxComplete( "" )
        else:
            self.textbox.setText( self._text )
            
            
    
    
'''