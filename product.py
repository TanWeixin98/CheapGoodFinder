import scrapy
#Used to store the price, rating and url of the product searched by the user. Additionally, can be used to stoer picture urls
class product(scrapy.item):
    price= scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    picture_url = scrapy.Field()