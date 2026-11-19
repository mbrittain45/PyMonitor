


from AppUtils import Logger, DTFmt
from FileSystem import AsyncFileTaskMgr, FileOperation


#
# HtmlTag - build tags as they are requested
#
class HtmlTag:


    @staticmethod
    def headPartialTag( tag: str ) -> str:
        return ("<" + tag)


    @staticmethod
    def headTag( tag: str ) -> str:
        return ("<" + tag + ">")


    @staticmethod
    def headTrailingTag() -> str:
        return ">"


    @staticmethod
    def endTag( tag: str ) -> str:
        return ("</" + tag + ">")
    

    # see if a tag exists
    @staticmethod
    def hasTag( html: str, tag: str ) -> bool:

        if html.find( tag ) == -1:
            return False
        return True
        

   # check for a complete tag ie '<tag>'
    @staticmethod
    def isHeadTag( html: str, tag: str ) -> bool:
        
        if html.find( HtmlTag.headTag(tag) ) != -1:
            return True

        return False
    



#
# Base HTML Parser
#
class BaseHtmlParser:

 
    # parse <tag...> to </tag> section
    @staticmethod
    def __getSepTag__( html: str, tag: str ) -> str:
    
        p1  = html.find( HtmlTag.headPartialTag(tag) )
        p1a = html.find( HtmlTag.headTrailingTag() )
        p2  = html.find( HtmlTag.endTag(tag) )
        
        if p1 == -1 or p1a == -1 or p2 == -1:
            return "Error -- Cannot find Tag Positions"
        elif p1a < p1 or p2 < p1:
            return "Error -- Tag Positions are Reversed"
        
        p1a += 1
        return html[ p1a : p2 ] 
   


    # parse <tag> to </tag> section
    @staticmethod
    def __getTag__( html: str, tag: str ):
        
        p1  = html.find( HtmlTag.headTag(tag) )
        p2  = html.find( HtmlTag.endTag(tag) )
        
        if p1 == -1 or p2 == -1:
            return "Error -- Cannot find Tag Positions"
        elif p2 < p1:
            return "Error -- Tag Positions are Reversed"
        
        return html[ (p1 + len( tag ) + 2) : p2 ] 
    

    # remove a tag
    @staticmethod
    def removeTag( html: str, tag: str ) -> str:
    
        endTag = HtmlTag.endTag(tag)

        p = html.find( endTag )
        if p == -1:
            return ""
        
        p += len( endTag )

        return html[ p : (len(html) - p) ] 
    

    # get a tag
    @staticmethod
    def getTag( html: str, tag: str ) -> str:
        
        retStr = ""

        if HtmlTag.hasTag( html, tag ) == False:
            Logger.err( f"BaseHtmlParser.getTag didn't find the requested tag: <{tag}> in html: {html}" )
            return retStr
        
        if HtmlTag.isHeadTag( html, tag ) == False:
            
            retStr = BaseHtmlParser.__getSepTag__( html, tag )
            if retStr.find( "Invalid" ) != -1:
                Logger.err( "BaseHtmlParser.__getSepTag__ returned: {} for html: {}".format( retStr, html ) )

        else:
            
            retStr = BaseHtmlParser.__getTag__( html, tag )
            if retStr.find( "Invalid" ) != -1:
                Logger.err( "BaseHtmlParser.__getTag__ returned: {} for html: {}".format( retStr, html ) )
        
        return retStr
 
    
 



#
# Html Parser
#
class HtmlParser:
    
    TBODY   = "tbody"       # table body
    DIV     = "div"         # divisor
    TROW    = "tr"          # table row
    TDATA   = "td"          # table data
    HLINK   = "a"           # hyperlink 'aref=
    MAIN    = "main"        # main body
    TITLE   = "title"       # title
    BODY    = "body"        # html body
    SUMMARY = "summary"     # summary
    DETAILS = "details"     # details
    

    # remove table body
    @staticmethod
    def removeTableBody( html: str ) -> str:

        return BaseHtmlParser.removeTag( html, HtmlParser.TBODY )
    
    
    # remove a division
    @staticmethod
    def removeDivision( html: str ) -> str:

        return BaseHtmlParser.removeTag( html, HtmlParser.DIV )
    

    # remove a table row
    @staticmethod
    def removeTableRow( html: str ) -> str:

        return BaseHtmlParser.removeTag( html, HtmlParser.TROW )
    
    
    # remove table data
    @staticmethod
    def removeTableData( html: str ) -> str:
        return BaseHtmlParser.removeTag( html, HtmlParser.TDATA )
    

    # remoe a hyperlink
    @staticmethod
    def removeHyperlink( html: str ) -> str:
        return BaseHtmlParser.removeTag( html, HtmlParser.HLINK )
    


    # parse a table row <tr></tr>
    @staticmethod
    def parseTableRow( html: str ) -> str:
        return BaseHtmlParser.getTag( html, HtmlParser.TROW )
    

    # parse out a table body
    @staticmethod
    def parseTableBody( html: str ) -> str:
        return BaseHtmlParser.getTag( html, HtmlParser.TBODY )
    

    # parse a division <div></div>
    @staticmethod
    def parseDivision( html: str ) -> str:
        return BaseHtmlParser.getTag( html, HtmlParser.DIV )
    

    # parse table data <td>...</td> or <td class="sym"><a href="/stocks/cflt/">CFLT</a></td>
    @staticmethod
    def parseTableData( html: str ) -> str:
        return BaseHtmlParser.getTag( html, HtmlParser.TDATA )
    

    # parse a hyperlink
    @staticmethod
    def parseHyperlink( html: str ) -> str:
        return BaseHtmlParser.getTag( html, HtmlParser.HLINK )
    

    # parse a table rows <tr></tr>
    @staticmethod
    def parseTableRows( html: str ) -> list[str]:
    
        elements = []
        
        while HtmlTag.hasTag( html, HtmlParser.TROW ):
            
            divElem = BaseHtmlParser.getTag( html, HtmlParser.TROW )
            elements.append( divElem )      # type: ignore
            html    = BaseHtmlParser.removeTag( html, HtmlParser.TROW )
            
        return elements    # type: ignore
    
    
    # parse out a table body
    @staticmethod
    def parseTableBodies( html: str ) -> list[str]:

        elements = []
        
        while HtmlTag.hasTag( html, HtmlParser.TBODY ):
            
            divElem = BaseHtmlParser.getTag( html, HtmlParser.TBODY )
            elements.append( divElem )  # type: ignore
            html    = BaseHtmlParser.removeTag( html, HtmlParser.TBODY )
            
        return elements    # type: ignore

    
    # parse a division <div></div>
    @staticmethod
    def parseDivisions( html: str ) -> list[str]:
        
        elements = []
        
        while HtmlTag.hasTag( html, HtmlParser.DIV ):
            
            divElem = BaseHtmlParser.getTag( html, HtmlParser.DIV )
            elements.append( divElem )      # type: ignore
            html    = BaseHtmlParser.removeTag( html, HtmlParser.DIV )
            
        return elements    # type: ignore

    
    # parse table datas <tdata>
    @staticmethod
    def parseTableDatas( html: str ) -> list[str]:
        
        elements = []
        
        while HtmlTag.hasTag( html, HtmlParser.TDATA ):
            
            divElem = BaseHtmlParser.getTag( html, HtmlParser.TDATA )
            elements.append( divElem ) # type: ignore
            html    = BaseHtmlParser.removeTag( html, HtmlParser.TDATA )
            
        return elements    # type: ignore

        
    # parse a tagged section and dump it to a file
    @staticmethod
    def parseSection( html: str, tag: str, fileName: str = "" ) -> str:
        
        startTag    = HtmlTag.headTag(tag)
        endTag      = HtmlTag.endTag(tag)
        
        p1          = html.find( startTag )
        p2          = html.find( endTag )
        
        if p1 != -1 and p2 != -1:

            section = html[ (p1 + len(startTag)) : (p2 - len(endTag)) ] 

            if len( fileName ) > 0:

                fileOp  = FileOperation.createWriteBloblFileOp( fileName, section, None, False ) # type: ignore
                AsyncFileTaskMgr.requestFileOp( fileOp )         # type: ignore

            return section

        else:
            assert( False )
    
    
    # get all hyperlinks in a page
    @staticmethod
    def parseAllHyperlinks( html: str ) -> list[str]:
        
        HREF_BEGIN_TAG = "<a href="
        HREF_END_TAG   = "\"a"
        
        hyperlinks: list[str] = []
        
        while len( html ) > 0:
            
            pos = html.find( HREF_BEGIN_TAG )
            if pos == -1:
                return hyperlinks
           
            pos += len( HREF_BEGIN_TAG )
            html = html[ pos : (len( html ) - pos) ]
            
            pos  = html.find( HREF_END_TAG )
            link = html[ 0 : pos ]
            
            hyperlinks.append( link )
            
        return hyperlinks


    # parse the title
    @staticmethod
    def parseTitle( html: str ) -> str:
        return HtmlParser.parseSection( html, HtmlParser.TITLE )
    

    # parse the body
    @staticmethod
    def parseBody( html: str ) -> str:
        return HtmlParser.parseSection( html, HtmlParser.BODY )
    

    # parse the summary
    @staticmethod
    def parseSummary( html: str ) -> str:

        summary = HtmlParser.parseSection( html, HtmlParser.SUMMARY )
        if len( summary ) <= 0:
            summary = HtmlParser.parseSection( html, HtmlParser.DETAILS )
        return summary
    

    # get published date
    @staticmethod
    def parsePublishDate( html: str ) -> str:

        pos = html.find( DTFmt.getYear() )
        if pos == -1:
            pos = html.find( DTFmt.getTwoDigitYear() )

        # find the end position
        epos = (pos + len( DTFmt.getYear() ))
        while True:

            if html[ epos + 1 ] != " ":
                epos += 1
            else:
                break;

        # find the starting position
        spos = pos
        while True:

            if html[ spos ] != " ":
                spos -= 1
            else:
                break;

        return html[ spos : epos ]
    
    
    # parse the main <main> table body <tbody> and return all table rows
    @staticmethod
    def parseMainTableBody( html: str ) -> str:
    
        main = HtmlParser.parseSection( html, HtmlParser.MAIN )
        if len( main ) > 0:
            
            tbody = HtmlParser.parseSection( html, HtmlParser.TBODY )
            if len( tbody ) > 0:
                return HtmlParser.parseTableRows( tbody )   # type: ignore
         
        assert( False )
        return []
    

    # parse the main <main>
    @staticmethod
    def parseMain( html: str ) -> str:
    
        return HtmlParser.parseSection( html, HtmlParser.MAIN )



