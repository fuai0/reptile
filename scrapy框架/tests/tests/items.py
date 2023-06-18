# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestsItem(scrapy.Item):
    # define the fields for your item here like:
    anthor = scrapy.Field()
    content = scrapy.Field()
    pass
