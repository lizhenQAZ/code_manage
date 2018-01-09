# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    rank = scrapy.Field()
    remark = scrapy.Field()
    brief = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
