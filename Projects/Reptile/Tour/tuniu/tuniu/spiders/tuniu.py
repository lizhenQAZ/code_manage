# -*- coding: utf-8 -*-
import time
import json
import re
import scrapy
from scrapy_redis.spiders import RedisSpider
from tuniu.items import TuniuItem


class TuniuSpider(RedisSpider):
    name = 'tuniu'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(TuniuSpider, self).__init__(*args, **kwargs)

    redis_key = 'tuniu'

    def parse(self, response):
        # 获取当前页码
        now_page = int(re.findall(r'page=(\d+)', response.url)[0])
        # print(now_page)
        # 获取响应，解析url
        str_data = response.body.decode('UTF-8', errors='ignore')
        # print(str_data)
        try:
            node_list = json.loads(str_data)['data']['rows']
            # print(node_list)
            for node in node_list:
                item = TuniuItem()
                item['title'] = node['name'].strip()
                item['views'] = node['viewCount']
                item['like'] = node['likeCount']
                item['link'] = 'http://www.tuniu.com/trips/' + str(node['id'])
                item['summary'] = node['summary'].strip()
                # print(item)
                # 根据需要判断是否需要提取详情页链接
                yield scrapy.Request(item['link'], callback=self.parse_detail, meta={'basic': item})
                # 翻页
            if len(node_list) != 0:
                next_page = now_page + 1
                next_url = 'http://trips.tuniu.com/travels/index/ajax-list?sortType=1&page=' + str(next_page) + '&limit=10'
                yield scrapy.Request(next_url, callback=self.parse)
            else:
                pass
        except Exception as e:
            print(e)

    def parse_detail(self, response):
        item = response.meta['basic']
        item['created_time'] = response.xpath('//span[@class="time"]/text()').extract_first().strip().split(':')[-1]
        item['update_time'] = response.xpath('//span[@class="update"]/text()').extract_first().strip().split(':')[-1]
        item['desc'] = '\n'.join(response.xpath('//p[@class="section-des"]/text()').extract())
        item['image'] = '\n'.join(response.xpath('//div[@class="section-img"]/img/@data-src').extract())
        addr = response.xpath('//a[@class="link_de"]/text()').extract_first()
        item['addr'] = addr.strip() if addr else ''
        item['time'] = time.ctime()
        # print(item)
        yield item
