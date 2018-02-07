#coding:utf-8
from selenium import webdriver
import json
import time

class Douyu(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.file = open('douyu.json','w')

    def parse_data(self):
        # 获取房间节点列表
        node_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li/a')
        # print(len(node_list))
        data_list = []
        for node in node_list:
            temp = {}
            temp['title'] = node.find_element_by_xpath('./div/div/h3').text
            temp['type'] = node.find_element_by_xpath('./div/div/span').text
            temp['owner'] = node.find_element_by_xpath('./div/p/span[1]').text
            temp['views'] = node.find_element_by_xpath('./div/p/span[2]').text
            temp['cover'] = node.find_element_by_xpath('./span/img').get_attribute('data-original')
            temp['url'] = node.get_attribute('href')
            data_list.append(temp)
        return data_list

    def save_data(self,data_list):
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):
        # 构建url
        # 构建浏览器驱动
        # 发起请求
        self.driver.get(self.url)
        while True:
            # 解析数据
            data_list = self.parse_data()
            # 保存数据
            self.save_data(data_list)
            # 点击下一页
            try:
                el_next = self.driver.find_element_by_xpath('//a[@class="shark-pager-next"]')
                el_next.click()
                time.sleep(3)
            except:
                break

if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
