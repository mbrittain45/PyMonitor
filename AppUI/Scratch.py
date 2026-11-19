'''


        # Row Buttons horizontal layout
        self.horizontalLayoutWidget = QWidget( self )
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )

        # Table Row buttons
        if self.funcData.rowDeletable:
            button = SimpleWidget.createPushButton( "Delete Row", self.horizontalLayoutWidget, "deleteRowButton" ) 
            button.clicked.connect( self.deleteRow )
            self.horizontalLayout.addWidget( button ) 
            button.setEnabled( True )
            
            button = SimpleWidget.createPushButton( "Restore Delete Row", self.horizontalLayoutWidget, "restoreDeletedRowButton" )
            button.clicked.connect( self.restoreDeletedRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.funcData.rowHideable:
            button = SimpleWidget.createPushButton( "Hide Row", self.horizontalLayoutWidget, "hideRowButton" )
            button.clicked.connect( self.hideRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Row", self.horizontalLayoutWidget, "restoreHiddenRowButton" )
            button.clicked.connect( self.restoreHiddenRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )
            
        if self.funcData.rowUpdateable:
            button = SimpleWidget.createPushButton( "Update Row", self.horizontalLayoutWidget, "updateRowButton" )
            button.clicked.connect( self.updateRow )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        #if funcData.rowReordering:
        #    vlayout.theLayout.addWidget( self.getPushButton( "Reorder Row", uilevel, self.reorderRowCB ) ) # type: ignore

        if self.funcData.rowHasPage:
            button = SimpleWidget.createPushButton( "View Row Page", self.horizontalLayoutWidget, "viewRowPageButton" )
            button.clicked.connect( self.viewRowPage )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

  
        # Column Buttons horizontal layout
        self.horizontalLayoutWidget2 = QWidget( AppAbbrvApi.getMainWidget() )
        self.horizontalLayoutWidget2.setObjectName(u"horizontalLayoutWidget2")
        self.horizontalLayoutWidget2.setGeometry( QRect(220, 800, 1021, 80) )

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout2")
        self.horizontalLayout.setContentsMargins( AppAbbrvApi.getButtonMargin() )
        
        if self.funcData.columnDeletable:
            button = SimpleWidget.createPushButton( "Delete Column", self.horizontalLayoutWidget, "deleteColumnButton" )
            button.clicked.connect( self.deleteColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Deleted Column", self.horizontalLayoutWidget, "restoreDeletedColumnButton" )
            button.clicked.connect( self.restoreDeletedColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        if self.funcData.columnHideable:
            button = SimpleWidget.createPushButton( "Hide Column", self.horizontalLayoutWidget, "hideColumnButton" )
            button.clicked.connect( self.hideColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

            button = SimpleWidget.createPushButton( "Restore Hidden Column", self.horizontalLayoutWidget, "restoreHiddenColumnButton" )
            button.clicked.connect( self.restoreHiddenColumn )
            self.horizontalLayout.addWidget( button )
            button.setEnabled( True )

        #if self.columnUpdateable = False
        #self.columnReordering = False

        SimpleWidget.createLabel( "Row Buttons", self )
        SimpleWidget.createLabel( "Column Buttons", self )

        self.show()

    
    # figure out new column reordering don't allow row zero to move
    def reorderColumns( self ):
        column_count = self.tableWidget.columnCount()
        column_names: list[str] = []
        for i in range(column_count):
            header_item = self.tableWidget.horizontalHeaderItem(i)
            if header_item is not None:
                column_names.append(header_item.text())
            else:
                column_names.append(str(i + 1)) # Default header names are usually just the column index + 1
        
    # ROW Slots

    @Slot()
    def deleteRow( self ):
        self.rowTracker.delete( self.tableWidget )

    @Slot()
    def restoreDeletedRow( self ):
        deletedRows = self.rowTracker.getDeleted()
        if len( deletedRows ) > 0:
            rowKey = self.displayNames( "Restore Row", "Choose Row to Restore:", deletedRows )
            if len( rowKey ) > 0:
                self.rowTracker.restoreDeleted( rowKey, self.tableWidget, self.funcData )

    @Slot()
    def hideRow( self ):
        self.rowTracker.hide( self.tableWidget )

    @Slot()
    def restoreHiddenRow( self ):
        hiddenRows = self.rowTracker.getHidden()
        if len( hiddenRows ) > 0:
            rowName = self.displayNames( "Restore Row", "Choose Row to Restore:", hiddenRows )
            if len( rowName ) > 0:
                self.rowTracker.restoreHidden( rowName, self.tableWidget, self.funcData )

    @Slot()
    def updateRow( self ):
        assert( False ) # todo:

    @Slot()
    def viewRowPage( self ):
        assert( False ) # todo:

    # COLUMN Slots
    
    @Slot()
    def deleteColumn( self ):
        self.columnTracker.delete( self.tableWidget )

    @Slot()
    def restoreDeletedColumn( self ):
        deletedRows = self.rowTracker.getDeleted()
        if len( deletedRows ) > 0:
            rowName = self.displayNames( "Restore Row", "Choose Row to Restore:", deletedRows )
            if len( rowName ) > 0:
                self.rowTracker.restoreDeleted( rowName, self.tableWidget, self.funcData )

    @Slot()
    def hideColumn( self ):
        self.columnTracker.hide( self.tableWidget )

    @Slot()
    def restoreHiddenColumn( self ):
        hiddenRows = self.rowTracker.getHidden()
        if len( hiddenRows ) > 0:
            rowName = self.displayNames( "Restore Row", "Choose Row to Restore:", hiddenRows )
            if len( rowName ) > 0:
                self.rowTracker.restoreHidden( rowName, self.tableWidget, self.funcData )


#    @Slot
#    def updateColumn( self ):
    




# Enable section moving for the whole header
self.tableWidget.horizontalHeader().setSectionsMovable(True)

# Connect the signal
self.tableWidget.horizontalHeader().sectionMoved.connect(self.keep_column_zero_fixed)

def keep_column_zero_fixed(self, logicalIndex, oldVisualIndex, newVisualIndex):
    # If the column being moved is column 0 OR a column was moved into position 0
    if oldVisualIndex == 0 or newVisualIndex == 0:
        # Block signals to prevent an infinite recursion loop
        self.tableWidget.horizontalHeader().blockSignals(True)
        
        # Move the section back to where it belongs
        # moveSection(visualIndex_from, visualIndex_to)
        self.tableWidget.horizontalHeader().moveSection(newVisualIndex, oldVisualIndex)
        
        self.tableWidget.horizontalHeader().blockSignals(False)
'''

   
