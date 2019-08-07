import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)
class main (scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Battery_(electricity)']

    def parse(self, response):
        print (response.css('h1#firstHeading::text').extract())
