#coding:utf-8
from api import get_page
import re
import json


class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        self.pattern = re.compile('<script>var props=(.*?)</script>',re.S)

    def par_data(self,str_data):
        result = self.pattern.findall(str_data)[0]
        # print (result)

        with open('3_36.json','wb') as f:
            f.write(result.encode())
        temp_data = re.sub(',locationnal={.*','',result)

        with open('3_36_1.json','wb') as f:
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

    def save_data(self,data_list):
        with open('3_36kr.json','wb')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                f.write(str_data.encode())


    def run(self,):
        # 构建一个url
        # 发送请求
        str_data = get_page(self.url)
        # 解析数据
        data_list = self.par_data(str_data)
        # 保存数据
        self.save_data(data_list)

if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()