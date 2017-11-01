# -*- coding: utf-8 -*-
import scrapy
from myspider002_tencent.items import Myspider002TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    # 修改起始的url
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取所有职位节点列表
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # node_list = response.xpath('//*[@id="position"]/div[1]/table/tr')
        # print (len(node_list))

        # 便利节点列表
        for node in node_list:
            # 创建item
            item = Myspider002TencentItem()

            # 抽取数据
            item['job_name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['link'] = 'http://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract_first()
            item['type'] = node.xpath('./td[2]/text()').extract_first()   # 提取第一个，如果没有自动置None
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['addr'] = node.xpath('./td[4]/text()').extract_first()
            item['time'] = node.xpath('./td[5]/text()').extract_first()
            # print (item)
            # 返回数据给引擎
            yield item

        # 翻页
        try:
            next_url = 'http://hr.tencent.com/' + response.xpath('//*[@id="next"]/@href').extract()[0]
            yield scrapy.Request(next_url, callback=self.parse)
        except:
            pass
