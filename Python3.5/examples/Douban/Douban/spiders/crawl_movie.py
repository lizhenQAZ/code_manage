# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem
import re


class CrawlMovieSpider(CrawlSpider):
    name = 'crawl_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        nodes = response.xpath('//ol[@class="grid_view"]/li')
        # print(nodes)
        for node in nodes[:1]:
            movie = DoubanItem()
            movie["name"] = node.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract_first()
            movie["director"] = re.sub(r'[\n\xa0]', '', node.xpath(
                './/div[@class="bd"]/p[@class=""]/text()').extract_first()).strip()
            movie["type"] = re.sub(r'[\n\xa0]', '', node.xpath(
                './/div[@class="bd"]/p[@class=""]/text()').extract()[1]).strip()
            movie["rank"] = node.xpath(
                './/span[@class="rating_num"]/text()').extract_first()
            movie["remark"] = re.match('\d+', node.xpath(
                './/div[@class="star"]/span[4]/text()').extract_first()).group()
            movie["brief"] = node.xpath(
                './/span[@class="inq"]/text()').extract_first()
            movie["url"] = node.xpath(
                './/div[@class="hd"]/a/@href').extract_first()
            yield movie
