# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from web.items import DoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # 修改起始的url
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print (response.url,'------')
        # 获取电影节点列表
        node_list = response.xpath('//div[@class="info"]')
        # print (len(node_list))

        # 遍历节点列表
        for node in node_list:
            # 构建item实例
            item = DoubanItem()

            # 抽取数据
            item['name'] = node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['info'] = ''.join([i.strip() for i in node.xpath('./div[2]/p[1]/text()').extract()]).replace('\xa0','')
            item['desc'] = node.xpath('./div[2]/p[2]/span/text()').extract_first()
            # print (item)
            # 将数据返回给引擎
            yield item
