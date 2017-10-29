import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # 传递处理结果
            yield {
                'text': quote.css('.text::text').extract_first(),
                'author': quote.css('.author::text').extract_first(),
                # 'tag': quote.css('.tags .tag::text').extract_first(),
                'tag': quote.css('.tags .tag::text').extract(),
            }
            # 递归实现
            next_page = response.css('li.next a::attr("href")').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
