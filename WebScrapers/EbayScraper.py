import csv
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AmazonScrapy(CrawlSpider):
    name = "EbayScrapper"
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
             callback="parse_item",
             follow=True),)
    #base_url="https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
    #test url
    start_urls=["https://www.ebay.com/sch/i.html?_from=R40&_nkw=toy&_sacat=0&LH_TitleDesc=0&LH_TitleDesc=0&_pgn=1&rt=nc"]

    # def setBaseURL(self,URL):
    # start_urls = URL
    # get the dir of the data storage
    current_dir_name = os.path.dirname(__file__)
    current_dir_Length = len(current_dir_name) - 11
    project_dir_name = current_dir_name[:current_dir_Length]
    # open csv writer
    file_name = os.path.join(project_dir_name, 'dataStorage/EbaySearch.csv')
    file = open(file_name, 'w')

    search_writer = csv.writer(file, delimiter=',')

    count=0
    def parse_item(self, response):
        class_selector ='#ListViewInner>li'
        #set page limit to scraper
        self.count = self.count + 1
        if self.count==5:
            self.rules =Rule(LinkExtractor(allow=(), restrict_css=('.next',)), follow=False)
        for item in response.css(class_selector):
            name_selector= 'h3>a ::text'
            price_selector= '.bold ::text'
            rank_selector='.star-ratings>a ::attr(aria-label)'
            url_selector='h3>a ::attr(href)'
            img_url_selector='a ::attr(href)'
            # self.search_writer.writerow([item.css(name_selector).extract_first(), item.css(price_selector).extract_first(), item.css(rank_selector).extract_first(),
            #                        item.css(url_selector).extract_first(),item.css(img_url_selector).extract_first()])

            yield {
                'name': item.css(name_selector).extract_first(),
                'price': item.css(price_selector).extract_first(),
                'ranking': item.css(rank_selector).extract_first(),
                'url': item.css(url_selector).extract_first(),
                'imgURL': item.css(img_url_selector).extract_first()
            }
