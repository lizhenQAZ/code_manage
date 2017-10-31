#coding:utf-8
import requests
from lxml import etree
import json
import threading
from queue import Queue

class Qiushi(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
        # self.url_list = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
        }
        self.file = open('qiushi.json','w')
        self.url_queue = Queue()
        self.response_queue = Queue()
        self.data_queue = Queue()



    def generate_url(self):
        # self.url_list = [ self.base_url.format(i) for i in range(1,14) ]
        for i in range(1,14):
            url = self.base_url.format(i)
            self.url_queue.put(url)

    def get_page(self):
        while True:
            url = self.url_queue.get()
            print ('正在获取%s的响应'%url)
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                self.response_queue.put(response.content)
            else:
                self.url_queue.put(url)
            self.url_queue.task_done()


    def parse_data(self):
        while True:
            print ('开始解析数据')
            response = self.response_queue.get()
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

            self.data_queue.put(data_list)
            self.response_queue.task_done()

    def save_data(self):
        while True:
            print ('开始保存数据')
            data_list = self.data_queue.get()
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                self.file.write(str_data)
            self.data_queue.task_done()


    def __del__(self):
        self.file.close()


    def run(self):
        # # 构建url列表
        # self.generate_url()
        # # print (self.url_list)
        # # 构建请求头
        # # 遍历url列表
        # for url in self.url_list:
        #     # 发起请求，获取响应
        #     response = self.get_page(url)
        #     # 解析
        #     data_list = self.parse_data(response)
        #     # 保存
        #     self.save_data(data_list)

        thread_list = []

        # 创建生成url的线程
        t_generate_url = threading.Thread(target=self.generate_url)
        thread_list.append(t_generate_url)

        # 创建获取相应的线程
        for i in range(3):
            t = threading.Thread(target=self.get_page)
            thread_list.append(t)

        # 创建解析响应的线程
        for i in range(3):
            t = threading.Thread(target=self.parse_data)
            thread_list.append(t)

        # 创建数据存储线程
        t_save_data = threading.Thread(target=self.save_data)
        thread_list.append(t_save_data)

        # 遍历循环列表启动线程
        for  t in thread_list:
            # 将线程设置为守护线程，设置为守护线程之后，子线程将会跟随主线程的结束而结束
            t.setDaemon(True)
            t.start()

        for q in [self.url_queue,self.response_queue,self.data_queue]:
            #设置主线程等待队列操作完毕再退出主线程
            q.join()






if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()