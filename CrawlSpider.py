import scrapy
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Palaist crawleri - scrapy runspider CrawlSpider.py
logging.getLogger('scrapy').setLevel(logging.WARNING)
class WikiCrawl(CrawlSpider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']

    rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item (self, response):
        print (response.url)
