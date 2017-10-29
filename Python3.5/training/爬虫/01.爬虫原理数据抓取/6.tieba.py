#coding:utf-8
import requests
import sys


class Tieba(object):
    def __init__(self, tieba_name, pn):
        self.tieba_name = tieba_name
        # self.base_url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn='%(tieba_name)
        self.base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(tieba_name)

        # self.url_list = []
        # for i in range(pn):
        #     url = self.base_url + str(i*50)
        #     self.url_list.append(url)
        self.url_list = [self.base_url + str(i*50) for i in range(pn)]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_data(self, data, number):
        filename = self.tieba_name + '_' + str(number) + '.html'
        with open(filename,'wb')as f:
            f.write(data)

    def run(self):
        # 构建url列表
        # 构建请求头
        # 遍历url列表
        for url in self.url_list:
            # 发起请求
            data = self.get_page(url)
            # 保存源码
            number = self.url_list.index(url)
            self.save_data(data, number)


if __name__ == '__main__':
    tieba_name = sys.argv[1]
    pn = sys.argv[2]

    tieba = Tieba(tieba_name, int(pn))
    tieba.run()
