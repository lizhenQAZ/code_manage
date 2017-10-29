#coding:utf-8
import requests
import json


class Trans(object):
    def __init__(self,word):
        self.url = 'http://fanyi.baidu.com/v2transapi'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
        self.post_data = {
            "from": "zh",
            "to": "en",
            "query": word,
            "transtype": "translang",
            "simple_means_flag": 3
        }

    def get_data(self):
        response = requests.post(self.url,headers=self.headers,data=self.post_data)
        return response.content

    def parse_data(self,data):
        str_data = data.decode()
        result = json.loads(str_data)['trans_result']['data'][0]['dst']
        print (result)


    def run(self):
        # 构建一个url
        # 构建一个请求头
        # 构建post数据
        # 发送请求获取响应
        data = self.get_data()
        # 解析数据
        self.parse_data(data)


if __name__ == '__main__':
    trans = Trans('人生苦短，我用python')
    trans.run()