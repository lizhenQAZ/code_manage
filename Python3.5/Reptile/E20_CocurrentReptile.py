# coding: utf-8
import time
import requests
from lxml import etree
import json
from queue import Queue
from gevent import monkey
import gevent

monkey.patch_all()


class DoudanSpider(object):
    def __init__(self, url, q):
        super(DoudanSpider, self).__init__()
        self.url = url
        self.q = q
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        }

    def run(self):
        self.parse_item()

    def parse_url(self):
        for i in range(3):
            try:
                return requests.get(self.url, headers=self.headers).content
            except Exception as e:
                print("[info]" + str(e) + "\n" + str(self.url))

    def parse_item(self):
        response = self.parse_url()
        html = etree.HTML(response)
        nodes = html.xpath('//*[@class="grid_view"]/li')
        time.sleep(2)
        for node in nodes:
            tmp = {}
            tmp["movie"] = node.xpath('.//*[@class="info"]//a/span/text()')[0]
            tmp["url"] = node.xpath('.//*[@class="info"]//a/@href')[0]
            self.q.put(json.dumps(tmp, ensure_ascii=False))
        print(1111)


def main():
    base_url = "https://movie.douban.com/top250"
    item_num = 250
    url_list = (base_url + "?start=" + str(index) + "&filter=" for index in range(0, item_num, 25))
    q = Queue()
    p_list = (gevent.spawn(DoudanSpider(url, q).run) for url in url_list)
    gevent.joinall(p_list)
    print(q.qsize())
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    t = time.time()
    main()
    print("[info]耗时:" + str(time.time() - t) + "s")
