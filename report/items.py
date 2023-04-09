# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReportItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image = scrapy.Field()
    datetime = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()

