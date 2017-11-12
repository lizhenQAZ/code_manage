# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider005ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据来源
    datasource = scrapy.Field()
    # 数据采集时间
    timestamp = scrapy.Field()
    # 公司名
    company = scrapy.Field()
    # 浏览人数
    views = scrapy.Field()
    # 企业性质
    type = scrapy.Field()
    # 企业规模
    number = scrapy.Field()
    # 简介
    desc = scrapy.Field()
    # 好评度
    praise = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 融资情况
    faince_info = scrapy.Field()
    # 排名
    rank = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 网站
    website = scrapy.Field()
    # 联系方式
    contact = scrapy.Field()
    # qq
    qq = scrapy.Field()
    pass

