# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider007XiechengItem(scrapy.Item):
    train_name = scrapy.Field()
    train_Type = scrapy.Field()
    start_station_name = scrapy.Field()
    end_station_name = scrapy.Field()
    strat_time = scrapy.Field()
    end_time = scrapy.Field()
    use_time = scrapy.Field()
    pre_sale_time = scrapy.Field()
    train_min_price = scrapy.Field()
    train_date = scrapy.Field()
    collect_time = scrapy.Field()
