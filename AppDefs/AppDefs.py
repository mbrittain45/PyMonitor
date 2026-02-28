

from enum import Enum


#
# Stock Alerts
#
class EAlert( Enum ):
    
    eLowPrice           = 1
    eHighPrice          = 2
    eCustomLowPrice     = 3
    eCustomHighPrice    = 4   
    eCustomLowPrice2    = 5
    eCustomHighPrice2   = 6
    eEarningsTime       = 7
    eCompanyNews        = 8
# EAlert


#
# Stock Data Fields
#
class EFields( Enum ):
    
    # skip 0 since position zero is used for file persistence formatting for class Stock
    eIndex          = 1
    eSymbol         = 2
    eCompany        = 3
    eIndustry       = 4
    eRating         = 5
    ePrice          = 6
    eMarketCap      = 7
    eRevenue        = 8
    eVolume         = 9
    eEarnings       = 10
    eNetIncome      = 11
    eShares         = 12
    eEPS            = 13
    ePE             = 14
    eForwardPE      = 15
    eDividend	    = 16
    eHiRange	    = 17
    eLoRange	    = 18
    eTarget         = 19
    eChange         = 20
    eDiff           = 21
    # these fields are only kept in our main all stocks listing for a stock or etf
    eNotes          = 22 # user notes area
    eRecords        = 23 # our special links to other records
    eNewsFeeds      = 24 # links to news feed items for this stock
    eRssFeeds       = 25 # links to rss feed items for this stock
    eMaxField       = 26 # must always be last
# EField    
    

#
# Strings for EField above
#     
FieldNames = [ 
    "",
    "Index",
    "Symbol",
    "Company",
    "Industry", 
    "Rating",
    "Price",
    "Market Cap",
    "Revenue", 
    "Volume",
    "Earnings",
    "Net Income",
    "Shares", 
    "EPS", 
    "PE",
    "Forward PE",
    "Dividend", 
    "High Range",  
    "Low Range",  
    "Target", 
    "Change", 
    "Difference" 
    ]
# STOCK_FIELD_NAMES



#
# App Data Types - these data types can be automatically persisted via QDataStream
#       therefore we have this enum so a list of data types can be passed w/ a list
#       of variables to be persisted.
#
class EDataType( Enum ):
    
    eBoolDT         = 1
    eIntDT          = 2
    eFloatDT        = 3
    eStringDT       = 4
    eRawDataDT      = 5
    eBytesDT        = 6
# EDataType - end    


