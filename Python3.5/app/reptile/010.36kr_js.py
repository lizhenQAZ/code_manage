# coding:utf-8
import re
import json
import requests


class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
        self.pattern = re.compile('<script>var props=(.*?)</script>',re.S)

    def get_page(self, url):
        response = requests.get(url, headers=self.headers, verify=False)
        return response.content.decode()

    def parse_data(self, str_data):
        result = self.pattern.findall(str_data)[0]
        # print (result)
        with open('010_36kr_js_1.json', 'wb') as f:
            f.write(result.encode())
        temp_data = re.sub(',locationnal={.*', '', result)
        with open('010_36kr_js_2.json','wb') as f:
            f.write(temp_data.encode())
        # 将json格式的字符串转换成字典
        dict_data = json.loads(temp_data)['feedPostsLatest|post']
        data_list = []
        for news in dict_data:
            temp = {}
            temp['title'] = news['title']
            temp['cover'] = news['cover']
            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        with open('010_36kr_js_3.json', 'wb')as f:
            for data in data_list:
                str_data = json.dumps(data, ensure_ascii=False) + ',\n'
                f.write(str_data.encode())

    def run(self):
        # 构建一个url
        # 发送请求
        str_data = self.get_page(self.url)
        # 解析数据
        data_list = self.parse_data(str_data)
        # 保存数据
        self.save_data(data_list)

if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
