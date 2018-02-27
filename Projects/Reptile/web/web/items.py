# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class ItcastItem(scrapy.Item):
    # 姓名
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 简介
    desc = scrapy.Field()


class TencentItem(scrapy.Item):
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


class DouyuItem(scrapy.Item):
    nick_name = scrapy.Field()
    # 唯一id
    uid = scrapy.Field()
    # 图片链接
    image_link = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片存储路径
    image_path = scrapy.Field()


class ZhiyoujiItem(scrapy.Item):
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


class AqiItem(scrapy.Item):
    city = scrapy.Field()
    # url
    url = scrapy.Field()
    # 数据采集时间
    timestamp = scrapy.Field()
    # 数据
    date = scrapy.Field()
    AQI = scrapy.Field()
    LEVEL = scrapy.Field()
    PM2_5 = scrapy.Field()
    PM10 = scrapy.Field()
    SO2 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3 = scrapy.Field()


class DoubanItem(scrapy.Item):
    # 电影名
    name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 电影信息
    info = scrapy.Field()
    # 简介
    desc = scrapy.Field()
