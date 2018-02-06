#coding:utf-8
import requests
from lxml import etree
import os
import json


class TiebaPicture(object):
    def __init__(self,tieba_name):
        self.url = "http://tieba.baidu.com/f?kw=%s"%(tieba_name)
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) '
        }

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_list_page(self, list_page):
        # 将响应数据转换成elemenet对象
        html = etree.HTML(list_page)
        node_list = html.xpath('//ul[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        # print (len(node_list))
        detail_list = []
        for node in node_list:
            temp = {}
            temp['title'] = node.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
            detail_list.append(temp)
        try:
            next_url = 'http:' + html.xpath('//a[@class="next pagination-item"]/@href')[0]
        except:
            next_url = None

        return detail_list, next_url

    def parse_detail_page(self, detail_page):
        html = etree.HTML(detail_page)
        image_list = html.xpath('//div[@id="j_p_postlist"]//div[@class="d_post_content j_d_post_content  clearfix"]/img/@src')

        return image_list

    def download(self, image_list):
        if not os.path.exists('image'):
            os.makedirs('image')
        for url in image_list:
            filename = 'image' + os.sep + '011_baidu_tieba_xpath_' + url.split('/')[-1]
            data = self.get_page(url)
            with open(filename, 'wb')as f:
                f.write(data)

    def save_data(self, data):
        with open('011_baidu_tieba_xpath.json', 'wb+') as f:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            f.write(str_data.encode())

    def run(self):
        # 起始的url
        # 构建请求头
        next_url = self.url
        while next_url:
            # 发起请求获取响应
            list_page = self.get_page(next_url)
            # 从列表页面的响应中抽取 详情页面的url和标题列表 下一页的链接
            detail_list, next_url = self.parse_list_page(list_page)
            # 编列详情页面列表
            for detail in detail_list:
                detail_url = detail['link']
                # 获取详情页面的响应
                detail_page = self.get_page(detail_url)
                # 从详情页面中获取图片列表
                image_list = self.parse_detail_page(detail_page)
                # 下载图片
                self.download(image_list)
                print (image_list)
                # 保存数据
                detail['images'] = image_list
                self.save_data(detail)
        # 翻页

if __name__ == '__main__':
    tieba = TiebaPicture('校花')
    tieba.run()
