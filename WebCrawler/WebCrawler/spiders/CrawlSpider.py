import scrapy
from ..items import WikiImages
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Palaist crawleri - scrapy crawl Wikipedia


class WikiCrawl(scrapy.spiders.CrawlSpider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_stuff', follow="True"),
    )
    count=0

    def parse_stuff (self, response):
        self.count+=1
        print('Visiting link nr: ' + str(self.count) + ' ' + response.url)
        if "wikipedia" in response.url:
            heading = response.css("h1#firstHeading::text").get()
            if heading is not None:
                with open("wiki.txt", 'a+') as f:
                    f.write(heading+"\r\n")
        pictures = WikiImages()
        img_urls = []
        for shortUrl in response.css("img::attr(src)").getall():
            img_urls.append('https:'+shortUrl)
        pictures["image_urls"]=img_urls
        return pictures
        
            
        
        

