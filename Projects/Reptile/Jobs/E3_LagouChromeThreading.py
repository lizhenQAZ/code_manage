# coding:utf-8
# 导入webdriver
from selenium import webdriver
import json
from threading import Thread
import threading


class Lagou(object):
    def __init__(self):
        # 获取浏览器对象
        self.driver = webdriver.Chrome()
        # 获取起始页url
        self.url = 'https://www.lagou.com/zhaopin/Python/1/'
        # 获取url列表
        self.url_list = []
        # 获取全部岗位信息
        self.all_list = []
        # 写入文件
        self.file = open('024_lagou_chrome.json', 'wb')

    def parse_detail_link(self, url):
        self.driver.get(url)
        el_list = self.driver.find_elements_by_xpath(
            '//a[@class="position_link"]')
        url_list = [el.get_attribute('href') for el in el_list]
        self.url_list.extend(url_list)
        return url_list

    def parse_detail(self, urls):
        t_list = []
        for url in urls:
            t = Thread(target=self.save_item, args=(url,))
            t_list.append(t)
        for t in t_list:
            t.start()
            t.join()

    def save_item(self, url):
        if mutex.acquire(True):
            temp = {}
            self.driver.get(url)
            print(url)
            temp['link'] = url
            temp['name'] = self.driver.find_element_by_xpath(
                '//div[@class="company"]').text
            temp['job'] = self.driver.find_element_by_xpath(
                '//div[@class="job-name"]').get_attribute('title')
            temp['salary'] = self.driver.find_element_by_xpath(
                '//span[@class="salary"]').text
            temp['exp'] = \
            self.driver.find_elements_by_xpath('//dd[@class="job_request"]//span')[
                2].text
            temp['edu'] = \
            self.driver.find_elements_by_xpath('//dd[@class="job_request"]//span')[
                3].text
            temp['type'] = \
            self.driver.find_elements_by_xpath('//dd[@class="job_request"]//span')[
                4].text
            temp['time'] = self.driver.find_element_by_xpath(
                '//p[@class="publish_time"]').text
            temp['advantage'] = ''.join([i.text for i in
                                         self.driver.find_elements_by_xpath(
                                             '//dd[@class="job-advantage"]/p')])
            temp['duty'] = ''.join([i.text for i in
                                    self.driver.find_elements_by_xpath(
                                        '//dd[@class="job_bt"]/div/p')])
            temp['location'] = ''.join([i.text for i in
                                        self.driver.find_elements_by_xpath(
                                            '//div[@class="work_addr"]')])
            self.all_list.append(temp)
            mutex.release()

    def save_file(self):
        for detail in self.all_list:
            str_data = json.dumps(detail, ensure_ascii=False) + ',\n'
            self.file.write(str_data.encode())
        self.file.close()

    def parse_next_link(self, url):
        self.driver.get(url)
        return self.driver.find_elements_by_xpath('//div[@class="pager_container"]/a')[
            -1].get_attribute('href')

    def run(self):
        # 获取链接
        next_url = self.url
        while next_url != 'javascript:;':
            print(next_url)
            # 获取响应，提取详情链接
            detail_urls = self.parse_detail_link(next_url)
            # 获取响应，记录详情信息
            self.parse_detail(detail_urls)
            # 翻页
            next_url = self.parse_next_link(next_url)
        self.driver.close()

    def __del__(self):
        print(len(self.all_list))
        # 保存数据到文件
        self.save_file()

if __name__ == '__main__':
    lagou = Lagou()
    mutex = threading.Lock()
    lagou.run()
