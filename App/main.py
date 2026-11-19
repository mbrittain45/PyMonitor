

from App import StockApp


if __name__ == "__main__":

    #request = TestRequest( "https://stockanalysis.com/stocks/hims/" )

    # the global stock application
    global theStockApp
    theStockApp = StockApp()

    # run the application
    ret = theStockApp.exec()

    print( f"Application returned: {ret}" )


