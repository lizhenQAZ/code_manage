# -*- coding: utf-8 -*-
import json
import datetime
import time
import scrapy
from xpinyin import Pinyin
from xiecheng.items import XiechengItem


class XiechengSpider(scrapy.Spider):
    name = 'xiecheng'
    allowed_domains = ['ctrip.com']
    # start_urls = ['http://trains.ctrip.com/']

    def __init__(self):
        super(XiechengSpider, self).__init__()
        self.post_url = 'http://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=getSearchList'
        self.post_data = {}

    def bind_data(self, t = ('shanghai', 'nanjing', '上海', '南京', '2017-11-25', '2017-11-25')):
        con = '{"IsBus":false,"Filter":"0","Catalog":"","IsGaoTie":false,"IsDongChe":false,"CatalogName":"","DepartureCity":"' + t[0] + '","ArrivalCity":"' + t[1] + '","HubCity":"","DepartureCityName":"' + t[2] + '","ArrivalCityName":"' + t[3] + '","DepartureDate":"' + t[4] + '","DepartureDateReturn":"' + t[5] + '","ArrivalDate":"","TrainNumber":""}'
        self.post_data["value"] = con

    def start_requests(self):
        self.bind_data()
        yield scrapy.FormRequest(url=self.post_url, formdata=self.post_data, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        # print(response.body.decode(encoding='gb2312'))
        for data in self.generate_post_data():
            # print(data)
            self.bind_data(data)
            yield scrapy.FormRequest(url=self.post_url, formdata=self.post_data, callback=self.parse_item, meta={"date": data[-1]})

    def generate_date(self):
        dates = [(datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 2)]
        # print(len(list(dates)), "*"*50)
        return dates

    def generate_city(self):
        p = Pinyin()
        lists = ('上海', '南京', '北京')
        cities = [(p.get_pinyin(l1, ''), p.get_pinyin(l2, ''), l1, l2) for l1 in lists for l2 in lists if l1 != l2]
        # print(len(list(cities)), cities, "="*50)
        return cities

    def generate_post_data(self):
        post_data = [(*city, dates, dates) for city in self.generate_city() for dates in self.generate_date()]
        # print(len(list(post_data)), "-"*50)
        return post_data

    def parse_item(self, response):
        train_date = response.meta['date']
        dict_data = json.loads(response.body.decode(encoding='gb2312'))
        # print(dict_data)
        # if dict_data['IsShowSnatch'] == True:
        for items in dict_data['TrainItemsList']:
            item = XiechengItem()
            item['train_name'] = items['TrainName']
            item['train_Type'] = items['TrainType']
            item['start_station_name'] = items['StartStationName']
            item['end_station_name'] = items['EndStationName']
            item['strat_time'] = items['StratTime']
            item['end_time'] = items['EndTime']
            item['use_time'] = items['UseTime']
            item['pre_sale_time'] = items['PreSaleDay']
            item['train_min_price'] = items['TrainMinPrice']
            item['train_date'] = train_date
            item['collect_time'] = time.ctime()
            yield item
