import scrapy

class product(scrapy.item):
    price= scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()