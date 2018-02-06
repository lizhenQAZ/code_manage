# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class DouyuSpiderMiddleware(object):
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


class UserAgentDownloaderMiddleware(object):
    def process_request(self, request, spider):
        import random
        from scrapy.conf import settings
        # 随机获取一个代理
        user_agent = random.choice(settings['USER_AGENT_LIST'])
        # print(user_agent, '-' * 200)
        request.headers['User-Agent'] = user_agent


class IPProxyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        import time
        import random
        import base64
        from scrapy.conf import settings
        from twisted.internet.error import DNSLookupError
        # 随机获取一个代理
        proxy = random.choice(settings['PROXY_LIST'])
        # print(proxy, '-' * 200)
        while True:
        # 判断代理是否需要认证，如果需要认证，执行认证操作
        # if proxy.has_key(''):
            try:
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
                return
            except DNSLookupError as e:
                time.sleep(60)
                print(e)


class ErrorDownloaderMiddleware(object):
    def process_response(self, request, response, spider):
        from scrapy.conf import settings
        # 同一个url出错超过三次做下记录
        if response.status != 200:
            print(request.url)
            error_url_list = settings['ERROR_URL_LIST']
            if request.url in error_url_list:
                error_url_list[request.url] += 1
                if error_url_list[request.url] >= 3:
                    with open("error3.txt", 'wb+') as f:
                        data = str(response.status) + ' ' + request.url + ' ' + response.url
                        f.write(data.encode())
            else:
                with open("error1.txt", 'wb+') as f:
                    data = str(response.status) + ' ' + request.url + ' ' + response.url
                    f.write(data.encode())
                error_url_list[request.url] = 1
            return request
        return response
