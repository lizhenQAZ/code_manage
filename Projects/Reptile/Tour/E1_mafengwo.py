# coding: utf-8
import json
import time
import random
from copy import deepcopy
import requests
from lxml import etree
from redis import StrictRedis


class MaFengWo(object):
    scenary = []

    def __init__(self, url):
        # 设置访问域
        self.domain = 'http://www.mafengwo.cn'
        # 设置起始url
        self.start_url = url
        # 设置请求头
        self.headers = {
            'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;"
                          " .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR "
                          "3.0.04506.30) ",
        }
        # 连接redis数据库
        self.rc = StrictRedis()

    # 5.解析每篇游记的详情页
    def parse_detail(self, city_url):
        detail_url = city_url['yj_url']
        print(detail_url)
        response = requests.get(detail_url, headers=self.headers)
        html = etree.HTML(response.content)
        try:
            yj_startday = html.xpath('//li[@class="time"]/text()')[1]
        except IndexError:
            return
        yj_day = html.xpath('//li[@class="day"]/text()')[1]
        try:
            yj_type = html.xpath('//li[@class="people"]/text()')[1]
        except IndexError:
            yj_type = ''
        try:
            yj_cost = html.xpath('//li[@class="cost"]/text()')[1]
        except IndexError:
            yj_cost = ''
        yj_text = html.xpath('//div[@class="_j_content_box"]//text()')
        yj_image = html.xpath('//div[@class="_j_content_box"]//img/@data-rt-src')
        city_url['yj_startday'] = yj_startday
        city_url['yj_day'] = yj_day
        city_url['yj_type'] = yj_type
        city_url['yj_cost'] = yj_cost
        city_url['yj_text'] = yj_text
        city_url['yj_image'] = yj_image
        tmp = deepcopy(city_url)
        self.scenary.append(tmp)
        self.rc.rpush('mafengwo', tmp)
        time.sleep(random.random()*2 + 1)

    # 4.获取指定的每个游记
    def parse_yj(self, first_url, city_url, page='1'):
        c_id = first_url.split('/')[-1].split('.')[0]
        c_url = city_url
        print(c_id, page)
        data_url = 'http://www.mafengwo.cn/gonglve/ajax.php?act=get_travellist'
        data = {
            'mddid': c_id,
            'pageid': 'mdd_index',
            'sort': '1',
            'cost': '0',
            'days': '0',
            'month': '0',
            'tagid': '0',
            'page': page,
        }
        response = requests.post(data_url, data=data, headers=self.headers)
        str_data = response.content.decode()
        dict_data = json.loads(str_data)
        html = dict_data['list']
        html = etree.HTML(html)
        nodes = html.xpath('//div[@class="tn-wrapper"]')
        # for node in nodes[:1]:
        for node in nodes:
            yj_url = self.domain + node.xpath('./dl/dt/a/@href')[-1]
            print(yj_url)
            yj_title = node.xpath('./dl/dt/a/text()')[-1]
            city_url['yj_url'] = yj_url
            city_url['yj_title'] = yj_title
            try:
                yj_desc = node.xpath('./dl/dd/a/text()')[0]
                city_url['yj_desc'] = yj_desc
            except IndexError:
                city_url['yj_desc'] = ''
            try:
                yj_view = node.xpath('./div/span[@class="tn-nums"]/text()')[0]
                city_url['yj_view'] = yj_view
            except IndexError:
                city_url['yj_view'] = '0'
            try:
                yj_praise = node.xpath('./div/span[@class="tn-ding"]/em/text()')[0]
                city_url['yj_praise'] = yj_praise
            except IndexError:
                city_url['yj_praise'] = '0'
            self.parse_detail(city_url)
        max_page = etree.HTML(dict_data['page']).xpath('//span[@class="count"]/span/text()')[0]
        # if int(page) < 2:
        # if int(page) < max_page:
        now_page = int(page) + 1
        self.parse_yj(first_url, c_url, page=str(now_page))

    # 3.获取每个城市攻略
    def parse_gv(self, city_url):
        c_url = city_url['gv_url']
        response = requests.get(c_url, headers=self.headers)
        html = etree.HTML(response.content)
        gv_title = html.xpath('//div[@class="gl_title"]/span/text()')
        gv_desc = html.xpath('//div[@class="jianjie"]/p/text()')[0]
        gv_image = html.xpath('//li[@class="scroll-content-item"]/a/img/@src')
        city_url['gv_title'] = gv_title
        city_url['gv_desc'] = gv_desc
        city_url['gv_image'] = gv_image
        first_url = self.domain + html.xpath('//div[@class="mdd_m"]/dl/dt/a/@href')[0]
        self.parse_yj(first_url, city_url)

    # 2.获取每个省的城市列表
    def parse_city(self, province_url):
        p_url = province_url['p_url']
        response = requests.get(p_url, headers=self.headers)
        html = etree.HTML(response.content)
        nodes = html.xpath('//div[@class="gl_list"]')
        # for node in nodes[:1]:
        for node in nodes:
            gv_name = node.xpath('./a/@title')[0]
            gv_url = self.domain + node.xpath('./a/@href')[0]
            gv_time = node.xpath('./div[@class="update_time"]/text()')[0]
            gv_download = node.xpath('./div[@class="down_cout"]/p/text()')[0]
            province_url['gv_name'] = gv_name
            province_url['gv_url'] = gv_url
            province_url['gv_time'] = gv_time
            province_url['gv_download'] = gv_download
            self.parse_gv(province_url)

    # 1.获取每个省列表
    def parse_province(self, html):
        html = etree.HTML(html)
        nodes = html.xpath('//div[@class="wrapper"]/div[4]/ol/li')
        tmp = {}
        # for node in nodes[:1]:
        for node in nodes:
            p_name = node.xpath('./a/text()')[0].split('(')[0]
            p_url = self.domain + node.xpath('./a/@href')[0]
            tmp['p_name'] = p_name
            tmp['p_url'] = p_url
            self.parse_city(tmp)

    def run(self):
        # 解析url，获取响应
        response = requests.get(self.start_url, headers=self.headers)
        # 存储所有的数据
        self.parse_province(response.content)
        # 存入redis数据库
        with open('mafengwo.json', 'wb+') as f:
            for detail in self.scenary:
                str_data = json.dumps(detail, ensure_ascii=False) + ',\n'
                f.write(str_data.encode())


if __name__ == '__main__':
    start_url = 'http://www.mafengwo.cn/gonglve/mdd-cn-0-0-1.html#list'
    mafengwo = MaFengWo(start_url)
    mafengwo.run()
