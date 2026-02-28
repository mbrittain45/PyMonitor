

from enum import Enum

# todo: use all these request pages some where

#
# Stock Analysis Url - get a certain URL for a stock ticker for stockanalysis.com
#
class StockAnalysisUrl:

    class EUrlType( Enum ):

        eOverview           = int(0)
        eIncome             = int(1)
        eBalanceSheet       = int(2)
        eCashflow           = int(3)
        eRatios             = int(4)
        eKPIs               = int(5)
        eForecast           = int(6)
        eStatistics         = int(7)
        eMarketCap          = int(8)
        eMetrics            = int(9)
        eRevenue            = int(10)
        eRevenueXSegment    = int(11)
        eIncomeXSegment     = int(12)
        eExpenses           = int(13)
        eDividend           = int(14)
        eHistory            = int(15)
        
    URLS = [ 
        "https://stockanalysis.com/stocks/{}/",
        "https://stockanalysis.com/stocks/{}/financials/",
        "https://stockanalysis.com/stocks/{}/financials/balance-sheet/",
        "https://stockanalysis.com/stocks/{}/financials/cash-flow-statement/",
        "https://stockanalysis.com/stocks/{}/financials/ratios/",
        "https://stockanalysis.com/stocks/{}/financials/metrics/",
        "https://stockanalysis.com/stocks/{}/forecast/",
        "https://stockanalysis.com/stocks/{}/statistics/",
        "https://stockanalysis.com/stocks/{}/market-cap/",
        "https://stockanalysis.com/stocks/{}/metrics/",
        "https://stockanalysis.com/stocks/{}/revenue/",
        "https://stockanalysis.com/stocks/{}/metrics/revenue-by-segment/",
        "https://stockanalysis.com/stocks/{}/metrics/operating-income-by-segment/",
        "https://stockanalysis.com/stocks/{}/metrics/operating-expense-breakdown/",
        "https://stockanalysis.com/stocks/{}/dividend/",
        "https://stockanalysis.com/stocks/{}/history/"
    ]


    # get a specific url by type
    @staticmethod
    def getUrl( urlType: EUrlType, stockSymbol: str ):

        url = StockAnalysisUrl.URLS[ urlType.value ]
        return url.format( stockSymbol )


 
    
