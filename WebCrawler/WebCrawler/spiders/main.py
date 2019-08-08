import scrapy
import logging

# Palaist crawleri - scrapy runspider main.py
# Palaist crawleri un ssaglabāt datus json failā - scrapy runspider main.py

logging.getLogger('scrapy').setLevel(logging.WARNING)
class QuotesSpider(scrapy.Spider):
    name = "quotes" 
    start_urls = [
            'https://en.wikipedia.org/wiki/Main_Page'
    ]
    count=0 
    with open("wiki.txt", 'a+') as f:
        f.write("The visited wikipedia pages: "+"\r\n")    

    def parse(self, response):
        if "wikipedia" in response.url:
            heading = response.css("h1#firstHeading::text").get()
            if heading is not None:
                with open("wiki.txt", 'a+') as f:
                    f.write(heading+"\r\n")
            
        self.count+=1
        print ('Currently visiting link nr ' + str(self.count) + ': '+ response.url)
        for href in response.css("a::attr(href)").getall():
            yield response.follow(href, callback=self.parse)    #response.follow ir ideāls veids kā ielikt rindā jaunu linku, jo tas saprot arī relatīvos url
