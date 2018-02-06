# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider004DouyuItem(scrapy.Item):
    nick_name = scrapy.Field()
    # 唯一id
    uid = scrapy.Field()
    # 图片链接
    image_link = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片存储路径
    image_path = scrapy.Field()
    pass
