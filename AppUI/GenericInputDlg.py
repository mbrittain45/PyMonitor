
# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget, QInputDialog, QDialog


class GenericInputDlg( QWidget ):


    def __init__( self, title: str, label: str, useList: bool, listItems: list[str] ):

        self.dlg: QInputDialog = QInputDialog( self )

        self.dlg.setWindowTitle( title )
        self.dlg.setLabelText( label )
    
        if useList:
            self.dlg.setComboBoxItems( listItems )
            self.dlg.setOption( QInputDialog.InputDialogOption.UseListViewForComboBoxItems )
        else:
            self.dlg.setOption( QInputDialog.InputDialogOption.UsePlainTextEditForTextInput )
            

    def displayDialog( self ):

        if self.dlg.exec() == QDialog.DialogCode.Accepted:
            return self.dlg.textValue()
            
        return ""
