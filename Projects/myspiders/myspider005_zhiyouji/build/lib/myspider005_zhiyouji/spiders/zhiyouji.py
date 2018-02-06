# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# ----1 导入分布式爬虫类
from scrapy_redis.spiders import RedisCrawlSpider
from myspider005_zhiyouji.items import Myspider005ZhiyoujiItem
import time


# class ZhiyoujiSpider(CrawlSpider):
# ----2 修改爬虫类
class ZhiyoujiSpider(RedisCrawlSpider):
    name = 'zhiyouji'
    # ----3 注销起始的url和允许的域
    # # 修改允许的域
    # allowed_domains = ['jobui.com']
    # # 修改起始的url
    # start_urls = ['http://www.jobui.com/cmp']

    # ----4 动态获取允许的域
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(ZhiyoujiSpider, self).__init__(*args, **kwargs)

    # ----5 redis_key
    redis_key = 'zhiyouji'

    rules = (
        # 翻页链接的提取规则
        Rule(LinkExtractor(allow=r'/cmp\?n=\d+#listInter'), follow=True),
        # 详情页面链接提取规则
        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item'),
    )

    def parse_item(self, response):
        print(self.allowed_domains, '--------')
        # 创建item实例
        item = Myspider005ZhiyoujiItem()
        # 提取数据存入到item中
        item['timestamp'] = time.time()
        item['datasource'] = response.url
        item['company'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first().strip()
        item['views'] = response.xpath('//div[@class="grade cfix sbox"]/div[1]/text()').extract_first().strip().split('人')[0]
        item['type'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()|//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[0].strip()
        item['number'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()|//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[-1].strip()
        item['desc'] = ''.join(response.xpath('//*[@id="textShowMore"]/text()').extract())
        item['praise'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()
        item['salary'] = response.xpath('//div[@class="swf-contB"]/div/h3/text()').extract_first()
        # 融资信息列表
        data_list = []
        node_list = response.xpath('//div[@class="jk-matter jk-box fs16"]/ul/li')
        # print (len(node_list))
        # 遍历节点列表
        for node in node_list:
            temp = {}
            temp['date'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['amount'] = node.xpath('./span[2]/text()').extract_first()
            temp['invest'] = node.xpath('./span[3]/text()').extract_first()
            data_list.append(temp)
        item['faince_info'] = data_list
        # 融资信息列表
        data_list = []
        node_list = response.xpath('//div[@class="fs18 honor-box"]/div')
        # print (len(node_list))
        # 遍历节点列表
        for node in node_list:
            temp = {}
            key = node.xpath('./a/text()').extract_first()
            temp[key] = node.xpath('./span[2]/text()').extract_first()
            data_list.append(temp)
        item['rank'] = data_list
        item['address'] = response.xpath('//dl[@class="dlli fs16"]/dd[1]/text()').extract_first()
        item['website'] = response.xpath('//dl[@class="dlli fs16"]/dd[2]/a/text()').extract_first()
        try:
            item['contact'] = response.xpath('//dl[@class="dlli fs16"]/div[1]/dd/text()').extract_first().replace('\xa0', '')
            item['qq'] = response.xpath('//span[@class="contact-qq"]/text()').extract_first().strip()
        except:
            item['contact'] = None
            item['qq'] = None
        # print (item)
        # 返回给引擎
        yield item
