

'''

    #   
    # UI View Types - basically a view type for each task type
    #
    class EViewType( Enum ):

        eMainWindow         = int(0)    # application info/status
        eTaskStatus         = int(1)    # list status of all running tasks

        eAllAmexStocks      = int(2)    # list all AMAX stocks
        eAllNyseStocks      = int(3)    # list all NYSE stocks
        eAllNasdaqStocks    = int(4)    # list all Nasdaq stocks

        eNewsFeed           = int(5)    # display new from various business news sites
        eNewsFeedUrls       = int(6)    # user input - add or edit 1urls
        eNewsSentiment      = int(7)    # news sentiment display



        eRssFeed            = int(4)    # display rss feed news
        eRssFeedUrls        = int(5)    # user input - add or edit 1urls

        eVolumeLeadersView  = int(6)    # daily volume leaders

        
        #eStockSummaries     = int(7)    # query interface
    #   eMonitoredStocks    = int(7)    # user input, which stocks should be monitored
        #eMonitoredPrices    = int(8)    # monitored stocks overview w/ news and other things
        #eDailyLosers        = int(9)    # daily losers....
        #eDailyWinners       = int(10)   # daily winners...
        #eFutureDailyLosers  = int(11)   # look at history of daily losers and try to guess who is next or due....
        
        #eFinancialsOverview = int(12)   # list interesting finds from the financial company searches
        #eBookValueOverview  = int(13)   # list interesting finds from the book value and earnings searches

        # todo: add more here

        # options and futures ??

        #eMovingAverages     = int(20)   # display moving averages w/ volumes ...
        #eGraphView          = int(21)   # graph view stock

        eMaxViews           = int(22)

    #
    # View Types Names
    #    
    ViewMenuTypes = [ 
    
        ("Task Status", "Ctrl+T"),
        ("News Feeds", "Ctrl+N"),
        ("News Feed URLs", "Ctrl+U"),
        ("RSS Feeds", "Ctrl+R"),
        ("RSS Feed URLs", "Ctrl+L"),
        ("All Stocks", "Ctrl+A"),
        
        #"Abbreviated All Stocks", 
        #"Monitored Stocks", 
        #"Daily Losers", 
        #"Daily Winners", 
        #"Weekly Losers", 
        #"Weekly Winners", 
        #"Plotter", 
        #"Graph"
    ]
    # VIEW_TYPES



    #   VIEWS = [ "RSS Feed Input", "RSS Feed News", "News Feed Data", "News", "All Stocks", "New Stocks", "Monitored Stocks Input", "Monitored Stocks",
    #          "Daily Winners", "Daily Losers", "Winners History", "Losers History", "Statistics Input", "Statistics", "Calculations", "Projection" ]
 







'''