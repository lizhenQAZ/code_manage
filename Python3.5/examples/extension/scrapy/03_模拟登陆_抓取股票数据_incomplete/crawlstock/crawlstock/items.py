# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlstockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_code = scrapy.Field()
    subscription_code = scrapy.Field()
    stock_brief = scrapy.Field()
    online_release_date = scrapy.Field()
    launch_date = scrapy.Field()
    release_sum = scrapy.Field()
    online_release_sum = scrapy.Field()
    release_price = scrapy.Field()
    pe_radio = scrapy.Field()
    pass
