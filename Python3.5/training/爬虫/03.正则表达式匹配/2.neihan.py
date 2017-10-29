#coding:utf-8
from api import get_page
import re
import json


class Neihan(object):
    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.pattern = re.compile('<a target="_blank" class="image share_url" href="(.*?)".*?<p>(.*?)</p>',re.S)

    def parse_data(self, str_data):
        result = self.pattern.findall(str_data)

        # 构建一个数据列表
        data_list = []
        # 遍历结果列表
        for url,content in result:
            temp = {}
            temp['url'] = url
            temp['content'] = content
            data_list.append(temp)

        return data_list

    def save_data(self,data_list):
        with open('neihan.json','wb')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                f.write(str_data.encode())

    def run(self):
        # 构建url
        # 发送请求
        str_data = get_page(self.url)
        # print (str_data)
        # 解析数据
        data_list = self.parse_data(str_data)
        # 保存数据
        self.save_data(data_list)


if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()
