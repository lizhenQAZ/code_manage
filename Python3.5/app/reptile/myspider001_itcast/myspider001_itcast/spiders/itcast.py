# -*- coding: utf-8 -*-
import scrapy
from myspider001_itcast.items import Myspider001ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 获取信息列表
        node_list = response.xpath('//div[@class="li_txt"]')
        # 遍历列表，传递数据
        for node in node_list:
            item = Myspider001ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['desc'] = node.xpath('./p/text()').extract_first()
            print(item)
            # yield item
