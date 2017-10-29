#coding:utf-8
import requests
import json

class Movie(object):
    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=100'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }  

    def get_data(self):
        response = requests.get(self.url,headers=self.headers, verify=False)
        return response.content.decode()

    def parse_data(self, data):
        movie_list = json.loads(data)['subject_collection_items']

        # 创建返回数据的列表
        data_list= []

        # 循环获取每一个电影的信息
        for movie in movie_list:
            temp = {}
            temp['title'] = movie['title']
            temp['url']= movie['url']
            data_list.append(temp)
        return data_list

    def save_data(self,data_list):
        with open('08_movie.json','wb')as f:
            for data in data_list:
                str_data = json.dumps(data, ensure_ascii=False) + ",\n"
                f.write(str_data.encode())

    def run(self):
        # 构建一个url
        # 构建请求头
        # 发送请求
        data = self.get_data()
        # 解析数据
        data_list =self.parse_data(data)
        # 保存数据
        self.save_data(data_list)


if __name__ == '__main__':
    movie = Movie()
    movie.run()
