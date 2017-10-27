# -*- coding: utf-8 -*-
import scrapy
from ..items import BookinfoItem


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['douban.com']
    start_urls = ['httpS://book.douban.com']

    def parse(self, response):
        item = BookinfoItem()
        origin_list = response.css("div.hd h2 span::text").extract()
        target_list = []
        print('==============================', type(target_list), target_list)
        for j in origin_list:
            if '\n' not in j:
                target_list.append(j)
        print('==============================', type(target_list), target_list)
        item['head'] = target_list
        yield item
