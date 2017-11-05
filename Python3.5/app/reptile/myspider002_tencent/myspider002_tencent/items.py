# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class Myspider002TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名
    job_name = scrapy.Field()
    # 详情页面链接
    link = scrapy.Field()
    # 职位类别
    type = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地点
    addr = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 工作职责
    duty = scrapy.Field()
    # 工作要求
    requirement = scrapy.Field()
