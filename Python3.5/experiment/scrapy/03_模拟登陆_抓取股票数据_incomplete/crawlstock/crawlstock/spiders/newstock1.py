# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlstockItem
from pprint import pprint
import re


class Newstock1Spider(scrapy.Spider):
    name = 'newstock1'
    # allowed_domains = ['']
    start_urls = ['http://vip.stock.finance.sina.com.cn/corp/view/vRPD_NewStockIssue.php?page=1&cngem=0&orderBy=NetDate&orderType=desc']
    """获取所有新股信息"""

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

        # 2.获取翻页的个数
        pages = response.xpath("//table[@class='table2']/tr/td/text()").re(r"共(\d*)页")[0]
        pprint(pages)

        for i in range(1, int(pages)+1):
            # 3.拼接url
            replaced_url = re.sub(r'page=\d*', "page="+str(i), self.start_urls[0])
            pprint(replaced_url)

            # 4.递归查询
            yield response.follow(replaced_url, self.parse)
