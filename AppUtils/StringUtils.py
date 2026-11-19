


from AppDefs import Defs, DirDefs
    

# String methods

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values from a dictionary in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

#
# String Utils
#
class StrUtils:


    # get a websites name from the url remove the www. and .com                                              
    @staticmethod
    def getWebsiteName( url: str ):

        tmp = url
        pos = tmp.find( "www." )
        pos += 4
        tmp = tmp[ pos : len(tmp) - pos ]
        pos = tmp.find( "." )
        return tmp[ 0 : pos ]


    # get a value and remove value and delimiter
    @staticmethod
    def getDelimValue( strVal: str, delim: str ):

        p       = strVal.find( delim )
        if p == -1:
            return "", ""

        retVal  = strVal[ 0 : p ]   # get value
        p       += 1
        strVal  = strVal[ p : len(strVal) - p ] # remove value from string

        return retVal, strVal # return both


    @staticmethod
    def cleanseNumberStr( fstr: str ) -> str:

        rstr = ""
        for ch in fstr:
            if (ch >= '0' and ch <= '9') or ch == '.' or ch == "-" or ch == "+":
                 rstr += ch
        return rstr
            


    # convert a string to a float
    @staticmethod
    def stringToFloat( fstr: str ) -> float:

        try:
            fVal = float( fstr )            
            return fVal
        except:
            rstr = StrUtils.cleanseNumberStr( fstr ) # type: ignore
            return StrUtils.stringToFloat( rstr )    # type: ignore


    # convert a string to an int
    @staticmethod
    def stringToInt( istr: str ) -> int:

        try:
            iVal = int( istr )            
            return iVal
        except:
            rstr = StrUtils.cleanseNumberStr( istr ) # type: ignore
            return StrUtils.stringToInt( rstr )      # type: ignore

            
                
    # get number values
    @staticmethod
    def stringsToNumbers( strValues: list[str] ) -> list[float]:

        fValues: list[float] = []
        for strVal in strValues:
        
            f = StrUtils.stringToFloat( strVal )
            fValues.append( f )

        return fValues


    # trim both end of a string
    @staticmethod
    def trim( trimStr: str ) -> str:

        trimStr.strip()
        return trimStr


    # trim left side of a string
    @staticmethod
    def ltrim( trimStr: str ) -> str:

        trimStr.lstrip()
        return trimStr


    # trim right side of a string
    @staticmethod
    def rtrim( trimStr: str ) -> str:

        trimStr.rstrip()
        return trimStr


    # clean a possible numeric string of '.' and '-' since those chars make it invalid numerically
    @staticmethod
    def cleanseNumericString( numStr: str ):

        p = numStr.find( '-' )
        if p != -1:
            numStr.replace( '-', '' )
    
        p = numStr.find( '.' )
        if p != -1:
            numStr = numStr[ 0 : p ]

        return numStr


    # is numeric '.' and '-' can make a number non-numeric
    @staticmethod
    def isStringNumeric( numStr: str ) -> bool:

        numStr = StrUtils.cleanseNumericString( numStr )
        return numStr.isnumeric()   


    # reverse a string
    @staticmethod
    def reverseString( normStr: str ) -> str:

        retStr = ''
        index  = len( normStr )
        index  -= 1

        while index > -1:
            retStr += normStr[ index ]
            index -= 1

        return retStr

     
    # get a soundEx return value 1-4
    @staticmethod
    def getSoundExValue( matches: int, length: int ):

        if matches == 0:
            return 0
        elif matches >= length:
            return 4
        elif matches >= (length / 2):
            return 3
        elif matches >= (length / 4):
            return 2
        else:
            return 1

    #
    # Compares two SOUNDEX values, and returns an integer value 1-4
    #
    @staticmethod
    def difference( str1: str, str2: str ):

        matches = int(0)
        index   = int(0)

        length  = len( str1 )
        if len( str2 ) > length:
            length = len( str2 )

        while index < length:

            if index < len( str1 ):
                c1 = str1[ index : index + 1 ] 
            else:
                return StrUtils.getSoundExValue( matches, length )

            if index < len( str2 ):
                c2 = str2[ index : index + 1 ] 
            else:
                return StrUtils.getSoundExValue( matches, length )

            if c1 == c2:
                matches += 1
            
            index += 1

        return StrUtils.getSoundExValue( matches, length )


    '''
    # get substr by position
    @staticmethod
    def getSubstrByPosition( argStr: str, endPos: int ):
        
        numStr = StrUtils.cleanseNumericString( argStr )
        if StrUtils.isStringNumeric( numStr ):
            return argStr[ 0 : int( numStr ) ]
        assert( False )
        return ''
    
    
    # get substr by positions
    @staticmethod
    def getSubstrByPositions( argStr, startPos, endPos ):
        
        numStr1 = StrUtils.cleanseNumericString( startPos )
        numStr2 = StrUtils.cleanseNumericString( endPos )

        if StrUtils.isStringNumeric( numStr1 ) and StrUtils.isStringNumeric( numStr2 ):
            return argStr[ int( numStr1 ) : int( numStr2 ) ]

        assert( False )
        return ''
    '''   


    # add spaces before capital letters in the string
    @staticmethod
    def spaceCamelCase( stringToSpace: str ) -> str:
        
        c = 0 
        retStr = ""

        for c in stringToSpace:

            if 65 <= c <= 90:   # type: ignore
                retStr += " "
            retStr += c     # type: ignore
            
        return retStr[ 1 : (len( retStr )  - 1) ]   # type: ignore


    # parse a paragraph into sentences
    @staticmethod
    def parseSentences( block: str ) -> list[str]:
        
        lines: list[str] = []
        
        blockLen    = len( block )
        while blockLen > 0:
            
            bFound = False
            
            for ending in Defs.SENTENCE_ENDINGS:
                
                pos = block.find( ending )
                if pos != -1:
                    
                    line = block[ 0: pos ]
                    lines.append( line )
                    
                    pos         += 1
                    blockLen    -= pos
                    block       = block[ pos : blockLen ]
                
                    bFound      = True
                    break
                            
            if bFound == False:
                lines.append( block )
                return lines

        return lines
    
    
    # remove any comment in a line where comments start with #
    @staticmethod
    def removeComment( line: str ) -> str:
        
        line.strip()
        p = line.find( '#' )
        if p != -1:
            line = line[ p + 1, (len( line ) - (p + 1)) ] # type: ignore
            line.strip()
        return line


    # parse key=value from file data
    @staticmethod
    def parseKeyValue( key: str, fdata: str ):
        
        pos = fdata.find( key )

        if pos != -1:
            pos   += len( key )
            return fdata[ pos : (len( fdata ) - pos) ]
        else:
            assert( False )
        
        return ""
    

    # parse key=value from file line 
    @staticmethod
    def parseIniKeyValue( fileline: str ) -> tuple[str, str]:
        
        pos = fileline.find( '=' )
        if pos == -1:
            return ( " ", " " )

        key         = fileline[ 0 : pos ]
        fileline    = fileline[ pos + 1 : (len( fileline ) - (pos + 1)) ]

        return ( key, fileline )


    
    # get a substring by delimiter and remove it from the string
    @staticmethod
    def getSubstr( strVal: str, strDelim: str ) -> tuple[str, str]:

        subStr = ""
        retStr = ""

        pos = strVal.find( strDelim )
        if pos == -1:
            return subStr, retStr

        epos   = (pos + len( strDelim ))

        subStr = StrUtils.trim( strVal[ 0 : pos ] )
        retStr = StrUtils.trim( strVal[ epos : (len( strVal ) - epos) ] )

        return ( subStr, retStr )


    # get the main string for a title from the file name
    @staticmethod
    def getFileNameNormalized( filePath: str ) -> str:

        pos1 = filePath.rfind( DirDefs.SEP )
        pos2 = filePath.rfind( "." )
        pos2 += 1

        text = filePath[ pos1 : pos2 ]
        return StrUtils.spaceCamelCase( text )


    # remove spaces from a string
    @staticmethod
    def removeSpaces( strVal: str ) -> str:

        retVal  = ""
        
        strValues = strVal.split( " " )
        for value in strValues:
            retVal += value

        return retVal



    # get the main url address
    def getMainUrlAddress( self, url: str ) -> str:

        p = url.find( "." )
        if p != -1:
            return url[ 0 : (p + 1) ]
        else:
            p = url.find( "/" )
            return url[ 0 : p ]



