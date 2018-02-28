# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class TuniuItem(scrapy.Item):
    # 文章标题
    title = scrapy.Field()
    # 浏览量
    views = scrapy.Field()
    # 点赞人数
    like = scrapy.Field()
    # 页面链接
    link = scrapy.Field()
    # 简介
    summary = scrapy.Field()
    # 采集时间
    time = scrapy.Field()
    # 发表时间
    created_time = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
    # 正文内容
    desc = scrapy.Field()
    # 正文图片
    image = scrapy.Field()
    # 图片路径
    image_path = scrapy.Field()
    # 位置
    addr = scrapy.Field()
