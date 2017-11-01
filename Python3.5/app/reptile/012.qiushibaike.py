# coding:utf-8
import requests
from lxml import etree
import json


class Qiushi(object):
    def __init__(self, page):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.page = page
        self.url_list = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
        }
        self.file = open('012_qiushibaike.json', 'wb')

    def generate_url(self):
        self.url_list = [self.base_url.format(i) for i in range(1, self.page + 1)]

    def get_page(self,url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_data(self, response):
        # 将源码转换成element对象
        html = etree.HTML(response)
        # 获取所有帖子节点列表
        node_list = html.xpath('//div[@id="content-left"]/div')
        # print (len(node_list))
        data_list = []
        # 遍历节点列表，从单个节点中抽取数据
        for node in node_list:
            temp = {}
            try:
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                temp['link'] = 'https://www.qiushibaike.com' + node.xpath('./div[1]/a[2]/@href')[0]
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
                temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon','')
            except:
                temp['user'] = '匿名用户'
                temp['link'] = None
                temp['age'] = None
                temp['gender'] = None
            temp['content'] = node.xpath('./a[1]/div/span/text()')[0].strip()
            data_list.append(temp)

        return data_list

    def save_data(self,data_list):
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(str_data.encode())

    def __del__(self):
        self.file.close()

    def run(self):
        # 构建url列表
        self.generate_url()
        # print (self.url_list)
        # 构建请求头
        # 遍历url列表
        for url in self.url_list:
            # 发起请求，获取响应
            response = self.get_page(url)
            # 解析
            data_list = self.parse_data(response)
            # 保存
            self.save_data(data_list)


if __name__ == '__main__':
    page = input("请输入最大页数: ")
    qiushi = Qiushi(int(page))
    qiushi.run()
