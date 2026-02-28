

import time

from pypdf import PdfReader # type: ignore

from AppBaseTask import Task, TaskParent
from AppUtils import Logger, GuardedDictionary


#
# PDF Reader
#
class PDFReader( Task ):

    def __init__( self, filePath: str, parent: TaskParent ):

        Task.__init__( self, "PDFReader", False, parent )

        self.pdfFile = filePath
        self.pdfText = ""
        self.pdfDict = GuardedDictionary()

        self.pdfReader = PdfReader( self.pdfFile ) # type: ignore

        self.__startTask__()
    

    # get dictionary
    def getDict( self ):

        return self.pdfDict


    # read the pdf file
    def processTask(self) -> bool:      # type: ignore

        time.sleep( .3 )

        try:
      
            index = 0
            while index < self.pdfReader.get_num_pages():

                pageObject = self.pdfReader.get_page( index )
                for key, val in pageObject.items():
                    self.pdfDict.addItem( key, val )

        except:
            Logger.err( "Excepted in PDFReaqder procesTask()" )
            assert( False )
            return False

        return True



''' todo:
#
# PDF Writer
#
class PdfWriter:

    @staticmethod
    def readPDF( pdfFilePath: str ) -> str:

        text = ""

        # Load the PDF
        reader = PdfReader( stream: pdfFilePath )
        
        index = 0
        while index < len( reader.pages ):

            page  = reader.pages[ index ]
            index += 1

            text  += page.extract_text()

        return text


'''