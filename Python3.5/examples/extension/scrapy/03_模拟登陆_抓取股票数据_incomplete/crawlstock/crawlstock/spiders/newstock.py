# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlstockItem
from pprint import pprint


class NewstockSpider(scrapy.Spider):
    name = 'newstock'
    # allowed_domains = ['']
    start_urls = ['http://vip.stock.finance.sina.com.cn/corp/go.php/vRPD_NewStockIssue/page/1.phtml']

    def parse(self, response):
        item = CrawlstockItem()
        # 1.跳过前两条提示信息, 获取整个页面的信息
        links = response.xpath("//table[@id='NewStockTable']/tr")
        pprint(links)
        for num, i in enumerate(links):
            if num >= 2:
                item['stock_code'] = i.css("td div::text").extract_first()
                item['subscription_code'] = i.css("td div::text").extract()[1]
                item['stock_brief'] = i.css("td div a::text").re(r'\s*(\S*)\s*')[0]
                item['online_release_date'] = i.css("td div::text").extract()[3]
                item['launch_date'] = i.css("td div::text").extract()[4]
                item['release_sum'] = i.css("td div::text").extract()[5]
                item['online_release_sum'] = i.css("td div::text").extract()[6]
                item['release_price'] = i.css("td div::text").extract()[7]
                item['pe_radio'] = i.css("td div::text").extract()[8]
                yield item
