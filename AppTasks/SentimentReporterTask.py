

'''

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#
# NLTK Report - data used to report our findings
#
class SentimentReport:

    class BlobReport:
        def __init__(self):
            self.polarity       = float(0.0)
            self.subjectivity   = float(0.0)
            
    class LineReport:
        def __init__(self):
            self.positive      = None
            self.sentiment     = None
        
    def __init__(self):
        self.lines    = []
        self.blob     = None
         
    def numOfLines(self):
        return len( self.lines )
    
    def isPositive(self):
        
        pos = int(0)
        for line in self.lines:
            if line.positive:
                pos += 1
           
        if pos >= (self.numOfLines / 2):
            return True
        return False
                    

#
# Sentiment Analyzer
#
class SentimentAnalyzer:
    
    # init our stop words
    def __init__(self) :
        self.stopWords      = set(stopwords.words('english'))
        
    
    # get the sentiment of a text blob and the sentences
    def getSentiment( self, textLines ) -> SentimentReport:
        
        report = SentimentReport()
        
        # create the blob of text
        blob = ""
        for line in textLines:
            blob += line
        
        # get the entire sentiment for the text blob
        report.blob = self.getTextBlobSentiment( blob )
        
        # process each line for sentiment
        for line in textLines:
            
            lineReport = SentimentReport.LineReport()
            
            if self.isPositiveText( line ) and not self.isNegativeText( line ):
                lineReport.positive = True
            elif not self.isPositiveText( line ) and self.isNegativeText( line ):
                lineReport.positive = False
            else:
                lineReport.positive = None
                
            lineReport.sentiment = self.analyzeSentiment( line )
            
            report.lines.append( lineReport )
            
        return report
    
                
    
    # analysis returns dictionary of negative, neutral and positive scores all = to 1.0
    def analyzeSentiment( self, textPage ) -> dict[str, float]:
        return SentimentIntensityAnalyzer().polarity_scores( textPage )
        
    # true if textPage is positive
    def isPositiveText( self, textPage: str ) -> bool:
        return SentimentIntensityAnalyzer().polarity_scores( textPage )["compound"] > 0
    
    # true if textPage is negative
    def isNegativeText( self, textPage: str ) -> bool:
        return SentimentIntensityAnalyzer().polarity_scores( textPage )["compound"] <= 0
    
    # get text blob sentiment
    def getTextBlobSentiment( self, textBlob: str ) -> SentimentReport.BlobReport:
        
        blobReport              = SentimentReport.BlobReport()
        blobReport.polarity     = TextBlob( textBlob ).sentiment.polarity
        blobReport.subjectivity = TextBlob( textBlob ).sentiment.subjectivity
        return blobReport
    
    
    # strip stop words
    def stripStopWords( self, lines ): 
        
        filteredLines = []
        for line in lines:
            
            line_tokens     = word_tokenize( line )
           
            filteredLine    = []     # [w for w in line_tokens if not w.lower() in self.stopWords ]           
            for word in line_tokens:
                if word not in self.stopWords:
                    filteredLine.append( word )
            filteredLines.append( filteredLine )
                
        return filteredLines
    
    
    
    
    
    
 
 '''