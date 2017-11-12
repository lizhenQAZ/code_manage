# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from myspider_douban.settings import USER_AGENT_LIST
from myspider_douban.settings import PROXY_LIST
from scrapy import signals
import random
import base64


class MyspiderDoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        # print(user_agent, '-' * 200)
        request.headers['User-Agent'] = user_agent


class RandomProxy(object):
    def process_request(self, request, spider):
        # 随机获取一个代理
        proxy = random.choice(PROXY_LIST)
        print(proxy, '-' * 200)
        # 判断代理是否需要认证，如果需要认证，执行认证操作
        # if proxy.has_key(''):
        if 'user_passwd' in proxy:
            # 对账号密码进行编码
            result = base64.b64encode(proxy['user_passwd'].encode())
            # 设置认证信息
            request.headers['Proxy-Authorization'] = "Basic " + result.decode()

            # 设置代理
            request.meta['proxy'] = proxy['ip_port']
        else:
            # 设置代理
            request.meta['proxy'] = proxy['ip_port']
