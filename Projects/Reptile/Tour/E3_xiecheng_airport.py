# coding: utf-8
import datetime
import urllib
import json
import time
import re
import requests
from lxml import etree
from redis import Redis
from selenium import webdriver


class XiechengAirport(object):
    def __init__(self, url, query_url, query_ticket_url):
        self.url = url
        self.query_url = query_url
        self.query_ticket_url = query_ticket_url
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        }
        self.rd = Redis()
        self.driver = webdriver.Chrome()

    def parse_code(self, area):
        query_url = self.query_url + '?channel=1&mode=1&f=2&key=' + urllib.parse.quote(area)
        # print(area, query_url)
        respose = requests.get(query_url, headers=self.headers)
        code = respose.json()['content']
        code = json.loads(code)['Data'][0]['Code']
        return code

    def parse_airport(self, areas):
        airports = []
        for area in areas:
            temp = {}
            temp['name'] = area
            temp['code'] = self.parse_code(area)
            airports.append(temp)
        return airports

    def parse_date(self, date):
        dates = []
        for i in range(366):
            temp = (date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
            dates.append(temp)
        return dates

    def parse_param(self):
        self.driver.get(self.query_ticket_url)
        time.sleep(3)
        flight = self.driver.find_element_by_xpath('//*[@id="searchBoxUl"]/li[2]')
        flight.click()
        time.sleep(1)
        departure = self.driver.find_element_by_xpath('//*[@id="FD_StartCity"]')
        start_date = self.driver.find_element_by_xpath('//*[@id="FD_StartDate"]')
        destination = self.driver.find_element_by_xpath('//*[@id="FD_DestCity"]')
        # 防止元素点不到
        search = self.driver.find_element_by_xpath('//*[@id="searchBox"]/div[2]')
        departure.clear()
        departure.send_keys("上海")
        start_date.send_keys("2017-11-28")
        destination.send_keys("北京")
        search.click()
        time.sleep(1)
        submit = self.driver.find_element_by_xpath('//*[@id="FD_StartSearch"]')
        submit.click()
        time.sleep(5)
        user = self.driver.find_element_by_xpath('//*[@id="sso_txtUid"]')
        pwd = self.driver.find_element_by_xpath('//*[@id="sso_txtPwd"]')
        submit_auth = self.driver.find_element_by_xpath('//*[@id="sso_btnSubmit"]')
        uname = input("用户名")
        upwd = input("密码")
        user.click()
        user.send_keys(uname)
        pwd.send_keys(upwd)
        content = re.findall(r'LogToken=([^&]*?)&amp;CK=([^"]*?)"', self.driver.page_source)[0]
        params = {}
        params['log_token'] = content[0]
        params['ck'] = content[1]
        submit_auth.click()
        cookies = {}
        cookies_list = self.driver.get_cookies()  # 这里返回的是一个更多信息的字典列表
        for infos in cookies_list:
            cookies[infos['name']] = infos['value']
        return cookies, params

    def run(self):
        response = requests.get(self.url, headers=self.headers)
        html = etree.HTML(response.content.decode(encoding='gbk'))
        # 获取当前日期
        now = datetime.datetime.now()
        # print(now)
        # 获取全国的机场
        areas = html.xpath('//*[@class="schedule_list clearfix"]/li/a/text()')
        # print(areas)
        # areas = ["浦东国际机场"]
        # 获取全国机场的代码
        airports = self.parse_airport(areas)
        # print(airports)
        # 获取全部订票日期
        dates = self.parse_date(now)
        # print(len(dates), dates)
        # 获取提取参数
        cookies, params = self.parse_param()
        # print(len(params), params)
        col_data = {}
        col_data['col_time'] = str(now)
        col_data['airports'] = airports
        col_data['date'] = dates
        col_data['param'] = params
        col_data['cookie'] = cookies
        print(col_data)
        self.rd.rpush('xc_airport', col_data)

if __name__ == '__main__':
    url = 'http://flights.ctrip.com/hot-airport.html'
    query_url = 'http://m.ctrip.com/restapi/soa2/12812/getpoicontent'
    query_ticket_url = 'http://www.ctrip.com/'
    xc = XiechengAirport(url, query_url, query_ticket_url)
    xc.run()
