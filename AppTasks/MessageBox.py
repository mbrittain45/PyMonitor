

'''


from PySide6.QtWidgets import QMessageBox, QLineEdit, QInputDialog

from AppUtils import StrUtils


#
# Message Box - handles all the various QMessageBox types
#
class MessageBox:
    
    @staticmethod
    def about( title, text, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel ):
        
        msgBox = QMessageBox()
        msgBox.about( None, title, text, buttons, defButton )
        return msgBox.exec()


    @staticmethod
    def critical( title, text, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel):
        
        msgBox = QMessageBox()
        msgBox.critical( None, title, text, buttons, defButton )
        return msgBox.exec()

        
    @staticmethod
    def info( title, text, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel ):
        
        msgBox = QMessageBox()
        msgBox.information( None, title, text, buttons, defButton )
        return msgBox.exec()


    @staticmethod
    def question( title, text, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel ):
        
        msgBox = QMessageBox()
        msgBox.question( None, title, text, buttons, defButton )
        return msgBox.exec()


    @staticmethod
    def warning( title, text, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel ):
        
        msgBox = QMessageBox()
        msgBox.warning( None, title, text, buttons, defButton )
        return msgBox.exec()

        
    @staticmethod
    def general( title, text, info, icon = QMessageBox.Information, buttons = (QMessageBox.Ok | QMessageBox.Cancel), defButton = QMessageBox.Cancel ):
        
        msgBox = QMessageBox()
        
        msgBox.setTitle( title )
        msgBox.setText( text )
        msgBox.setIcon( icon )
        
        if len( info ) > 0:
            msgBox.setInformativeText( info )
            
        msgBox.setStandardButtons( buttons )
        msgBox.setDefaultButton( defButton )
        
        ret = msgBox.exec()
        if ret == QMessageBox.Ok:
            return msgBox.text()

        return None # cancel out

        

    @staticmethod
    def getTextInput( title: str, label:str, text: str ):

        # def getText (parent, title, label[, echo=QLineEdit.Normal[, text=””[, flags=Qt.WindowFlags()[, inputMethodHints=Qt.ImhNone]]]])
        return QInputDialog().getText( None, title, label, QLineEdit.Normal, text )
    


    @staticmethod
    def getUniqueTextInput( title: str, existingValues: list[ str ] ):

        lowerExistingValues = []
        for value in existingValues:
            lowerExistingValues.append( value.lower() )

        text     = ''
        theTitle = ('Get unique ' + title + ' value')
        label    = "Enter an Unique: {} value".format( title.upper() )

        while True:

            text, ok = MessageBox.getTextUserInput( theTitle, label, text ) 
            if ok and text:
            
                # see if the text is unique
                unique = True
                for value in existingValues:
                    if value == text:
                        unique = False
                        break

                # check again in lower case
                lowerText = text.lower()
                for lowerValue in lowerExistingValues:
                    if lowerValue == lowerText:
                        unique = False
                        break

                # if unique return the value
                if unique:
                    return text

                # value wasn't unique so make one for them
                text = StrUtils.makeValueUnique( text )

            elif not ok:
                return None
                
        return None # error



'''