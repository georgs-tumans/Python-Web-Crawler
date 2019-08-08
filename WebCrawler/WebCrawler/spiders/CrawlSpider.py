import scrapy
import sys
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Palaist crawleri - scrapy runspider CrawlSpider.py
# Palaist ar ierakstīšanu json failā - scrapy runspider CrawlSpider.py -o test.json
logging.getLogger('scrapy').setLevel(logging.WARNING)
count=0

class WikiCrawl(CrawlSpider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']

    rules = (
        Rule(LinkExtractor(allow_domains='en.wikipedia.org'), callback='parse_item', follow=True),
    )

    def parse_item (self, response):
        global count
        count = count + 1 
        print ('Number: '+ str(count) + ' '+ response.url)
        yield {'Link' : response.url}
        
            
        
        

