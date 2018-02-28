# coding: utf-8
import requests
import json


class XiechengSpider(object):
    def __init__(self):
        self.t = ('上海', '南京', '2017-11-25', '2017-11-25')
        self.url = 'http://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=getSearchList'
        self.con = '{"IsBus":false,"Filter":"0","Catalog":"","IsGaoTie":false,"IsDongChe":false,"CatalogName":"","DepartureCity":"shanghai","ArrivalCity":"nanjing","HubCity":"","DepartureCityName":"' + self.t[0] + '","ArrivalCityName":"' + self.t[1] + '","DepartureDate":"' + self.t[2] + '","DepartureDateReturn":"' + self.t[3] + '","ArrivalDate":"","TrainNumber":""}'
        # self.con = '{"IsBus":false,"Filter":"0","Catalog":"","IsGaoTie":false,"IsDongChe":false,"CatalogName":"","DepartureCity":"shanghai","ArrivalCity":"nanjing","HubCity":"","DepartureCityName":"上海","ArrivalCityName":"南京","DepartureDate":"2017-11-25","DepartureDateReturn":"2017-11-25","ArrivalDate":"","TrainNumber":""}'
        self.data = {"value": self.con}
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        }

    def run(self):
        response = requests.post(url=self.url, data=self.data, headers=self.headers)
        print(response.content.decode(encoding='gb2312'))
        with open("xiecheng.json", 'wb') as f:
            f.write(response.content.decode(encoding='gb2312').encode())

if __name__ == '__main__':
    xc = XiechengSpider()
    xc.run()
