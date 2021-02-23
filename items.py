# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PdvlabinternalsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mobile_name = scrapy.Field()
    mobile_price = scrapy.Field()
    mobile_rating = scrapy.Field()
    mobile_deliverytype = scrapy.Field()
    pass

