# -*- coding: utf-8 -*-
import scrapy
from ..items import TestimateItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        item = TestimateItem()
        for quote in response.css('div.quote'):
            # 传递处理结果
            item['text'] = quote.css('.text::text').extract_first(),
            item['author'] = quote.css('.author::text').extract_first(),
            item['tag'] = quote.css('.tags .tag::text').extract(),
            yield item
        # 递归实现
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
