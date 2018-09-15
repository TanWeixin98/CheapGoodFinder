import csv
import os
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
    # get the dir of the data storage
    current_dir_name = os.path.dirname(__file__)
    current_dir_Length = len(current_dir_name) - 11
    project_dir_name = current_dir_name[:current_dir_Length]
    # open csv writer
    file_name = os.path.join(project_dir_name, 'dataStorage/AmazonSearch.csv')
    file = open(file_name, 'w')

    search_writer = csv.writer(file, delimiter=',')
    def parse_item(self,response):
        class_selector ='.s-item-container'
        for item in response.css(class_selector):
            name_selector= 'a>h2 ::text'
            price_selector= '.a-offscreen ::text'
            rank_selector='a>i ::text'
            url_selector='a::attr(href)'
            img_url_selector='a>img::attr(src)'
            self.search_writer.writerow([item.css(name_selector).extract_first(), item.css(price_selector).extract_first(), item.css(rank_selector).extract_first(),
                                   item.css(url_selector).extract_first(),item.css(img_url_selector).extract_first()])






