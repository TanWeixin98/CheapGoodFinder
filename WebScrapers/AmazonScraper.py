from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AmazonScrapy(CrawlSpider):
    name = "AmazonSpider"
    accepted_domain="www.Amazon.com"
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagnNext',)),
             callback="parse_item",
             follow=True),)
    #test url
    start_urls=["https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=shoe"]

    # def setBaseURL(self,URL):
    #     start_urls = URL

    def parse_item(self,response):
        print("url"+response.url)
