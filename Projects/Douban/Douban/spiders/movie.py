# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem
import re


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        nodes = response.xpath('//ol[@class="grid_view"]/li')
        # print(nodes)
        for node in nodes[:1]:
            movie = DoubanItem()
            movie["name"] = node.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            movie["director"] = re.sub(r'[\n\xa0]', '', node.xpath('.//div[@class="bd"]/p[@class=""]/text()').extract_first()).strip()
            movie["type"] = re.sub(r'[\n\xa0]', '', node.xpath('.//div[@class="bd"]/p[@class=""]/text()').extract()[1]).strip()
            movie["rank"] = node.xpath('.//span[@class="rating_num"]/text()').extract_first()
            movie["remark"] = re.match('\d+', node.xpath('.//div[@class="star"]/span[4]/text()').extract_first()).group()
            movie["brief"] = node.xpath('.//span[@class="inq"]/text()').extract_first()
            movie["url"] = node.xpath('.//div[@class="hd"]/a/@href').extract_first()
            yield scrapy.Request(movie["url"], self.parse_detail, meta={"movie": movie})
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = self.start_urls[0] + next_url
            yield scrapy.Request(next_url, self.parse)

    def parse_detail(self, response):
        # print(response.url)
        movie = response.meta['movie']
        movie['content'] = ''.join([re.sub(r'[\n\u3000]', '', item).strip() for item in response.xpath('//*[@id="link-report"]/span[1]/span/text() | //*[@id="link-report"]/span[1]/text()').extract()])
        yield movie
