# -*- coding: utf-8 -*-
import scrapy
import json


class DouyuImageSpider(scrapy.Spider):
    name = 'douyu_image'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset='
    offset = 0
    start_urls = [base_url]

    def parse(self, response):
        print(response.encoding)
        json_data = json.loads(response.body.decode())
        print(json_data)
