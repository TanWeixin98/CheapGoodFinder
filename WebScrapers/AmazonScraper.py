import scrapy
import csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AmazonScrapy(CrawlSpider):
    name = "AmazonSpider"
    accepted_domain="www.Amazon.com"
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagnNext',)),
             callback="parse_item",
             follow=True),)
    base_url="https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
    #test url
    start_urls=["https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=toy"]

    # def setBaseURL(self,URL):
    #     start_urls = URL

    def parse_item(self,response):
        file_name = open('dataStorage/AmazonSearch.csv', 'w')
        search_writer = csv.writer(file_name, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        class_selector ='.s-item-container'
        for item in response.css(class_selector):
            name_selector= 'a>h2 ::text'
            price_selector= '.a-offscreen ::text'
            rank_selector='a>i ::text'
            url_selector='a::attr(href)'
            img_url_selector='a>img::attr(src)'
            yield {
                'name': item.css(name_selector).extract_first(),
                'price': item.css(price_selector).extract_first(),
                'ranking': item.css(rank_selector).extract_first(),
                'url': item.css(url_selector).extract_first(),
                'imgURL': item.css(img_url_selector).extract_first()
            }




