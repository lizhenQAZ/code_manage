# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class Myspider001ItcastItem(scrapy.Item):
    # 姓名
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 简介
    desc = scrapy.Field()
