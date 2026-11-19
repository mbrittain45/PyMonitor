
''' todo:

from StockWatcherMain import theApp

#
# Sitemap Reader
#
class SitemapReader:
    
    # init ourself
    def __init__(self):
        self._savedSiteMapUrlPairs = []     # pair holds base url and sitemap page url once its known
        self._notFoundSiteMapUrls = []
        
        self._baseWebsiteUrls = theApp.getWebsiteBaseUrls()
        self.loadSavedSiteMapUrls()


    # load our saved sitemap urls
    def loadSavedSiteMapUrls(self):
        
        f = open( ".\\Data\\SavedSiteMapUrls.dat", "r" )
        fileLines = f.readlines()
        f.close()
        
        for urlLine in fileLines:
            urlLine.strip()
            pos = urlLine.find( "," )
            self._savedSiteMapUrlPairs.append( ( urlLine[ 0 : pos ], urlLine[ pos + 1 : len(urlLine) ] ) )
        
            

    # write out a newly found sitemap urls
    def saveNewlyFoundSiteMapUrl(self, url):
        
        f = open( ".\\Data\\SavedSiteMapUrls.dat", "a" )
        try:
            f.write( url + "\n" )
            self._savedSiteMapUrls.append( url )
        except:
            print( "Excepted in SiteMapReader::saveNewlyFoundSiteMapUrl" )
        f.close()
            
            
    # find a saved site map url matching this url
     
    
    # set a copy of the web site urls
    def setWebsiteUrls( self, siteUrls ):
        

        for baseUrl, siteMapUrl in siteMapUrlPairs:

    
    # process the web site list
    def processWebsiteUrls( self, siteMapUrlPairs )

        
        for baseUrl, siteMapUrl in siteMapUrlPairs:
            
            if len( siteMapUrl ) == 0:
                
                siteMapUrl = self.findSavedSiteMapUrl( baseUrl )
                
                if len(knownSiteMapUrl) == 0:
                knownSiteMapUrl = figureOutSiteMapUrl( websiteUrl )
                if len(knownSiteMapUrl) == 0:
                    Log.log( )
                    continue    # couldn't find the site map page
            
                
    def readWebSiteSiteMap( self, baseurl ):
        
sitemap_url = "https://www.example.com/sitemap.xml"


Where to Find Sitemaps
Most websites provide a sitemap accessible at the following standard locations:

https://www.example.com/sitemap.xml
https://www.example.com/sitemap_index.xml
https://www.example.com/robots.txt
The robots.txt file often includes a reference to the sitemap, which you can find under the "Sitemap:" directive.


import requests

sitemap_url = "https://www.example.com/sitemap.xml"
response = requests.get(sitemap_url)

if response.status_code == 200:
    sitemap_content = response.text
else:
    print(f"Failed to fetch sitemap from {sitemap_url}")
    

from lxml import etree

sitemap_xml = etree.fromstring(sitemap_content.encode())


urls = sitemap_xml.xpath("//loc/text()")

for url in urls:
    print(url)
    

Step 4: Scrape Data from the URLs
With the URLs extracted from the sitemap, you can now use web scraping libraries like Beautiful Soup or Scrapy to fetch and parse the content from each URL:

from bs4 import BeautifulSoup

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")
        
        # Extract data from the page using Beautiful Soup
        # ...
        
        
        '''