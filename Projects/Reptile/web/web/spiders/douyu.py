# -*- coding: utf-8 -*-
import scrapy
from web.items import DouyuItem
import json


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset='
    offset = 0
    start_urls = [base_url]

    def parse(self, response):
        # 将相应数据中的json转换成Python字典
        data_list = json.loads(response.body.decode())['data']

        # 遍历房间列表
        for data in data_list:
            # 创建item
            item = DouyuItem()
            # 提取数据存储到item中
            item['nick_name'] = data['nickname']
            item['uid'] = data['owner_uid']
            item['image_link'] = data['vertical_src']
            item['city'] = data['anchor_city']
            # print (item)
            # 将数据返回给引擎
            yield item

        # 模拟下一页
        if len(data_list) != 0:
            self.offset += 100
            next_url = self.base_url + str(self.offset)
            # 发送请求
            yield scrapy.Request(next_url, callback=self.parse)
