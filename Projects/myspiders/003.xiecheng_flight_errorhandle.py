# coding: utf-8
import requests
import redis
import json
import time
import datetime
import random


class XiechengTicket(object):
    def __init__(self):
        self.collect_time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.rd = redis.Redis()
        self.rd2 = redis.Redis(db=1)
        self.rd3 = redis.Redis(db=2)
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        }

    def parse_code(self, codes):
        res_codes = []
        for i in codes:
            for j in codes:
                if i != j:
                    res_codes.append((i, j))
        return res_codes

    def parse_data(self, urls, cookies):
        temp_data = []
        while True:
            for url in urls:
                cookies['FD_SearchHistorty'] = str(cookies['FD_SearchHistorty'])
                response = requests.get(url, headers=self.headers, cookies=cookies)
                time.sleep(random.random())
                lis = response.json()['fis']
                for li in lis:
                    temp = {}
                    temp['acc'] = li['acc']
                    temp['acn'] = li['acn']
                    temp['apbn'] = li['apbn']
                    temp['at'] = li['at']
                    temp['dcc'] = li['dcc']
                    temp['dcn'] = li['dcn']
                    temp['dpbn'] = li['dpbn']
                    temp['dt'] = li['dt']
                    temp['fn'] = li['fn']
                    temp['pr'] = li['pr']
                    temp['tax'] = li['tax']
                    temp['cf'] = {'c': li['cf']['c'], 'dn': li['cf']['dn'], 's': li['cf']['s']}
                    conforts = json.loads(li['confort'])
                    temp['confort'] = {'dapart_bridge': conforts['DepartBridge'], 'history_punctuality': conforts['HistoryPunctuality'], 'history_punctuality_arr': conforts['HistoryPunctualityArr']}
                    scss = li['scs']
                    temp_price = []
                    for scs in scss:
                        temp_scs = {}
                        temp_scs['rt'] = scs['rt']
                        temp_scs['salep'] = scs['salep']
                        temp_price.append(temp_scs)
                    temp['scs'] = temp_price
                    temp['time'] = time.ctime()
                    temp['url'] = url
                    # print(temp)
                    time.sleep(random.random())
                    if temp not in temp_data:
                        temp_data.append(temp)
                        self.rd3.rpush(self.collect_time, temp)

    def run(self):
        datas = self.rd.lrange("xc_airport", 0, -1)
        data = json.loads(datas[0].decode().replace("'{", "{").replace("}'", "}").replace("'", "\""))
        cookies = data['cookie']
        datas = self.rd2.lrange("error", 0, -1)
        urls = []
        for data in datas:
            data = json.loads(data.decode().replace("'", "\""))
            for url, error in data.items():
                # print(url)
                urls.append(url)
        self.parse_data(urls, cookies)

if __name__ == '__main__':
    xc = XiechengTicket()
    xc.run()
