# coding: utf-8
import requests
import redis
import json
import time
import datetime
import random


class XiechengTicket(object):
    def __init__(self, url):
        self.collect_time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.url = url
        self.rd = redis.Redis()
        self.rd2 = redis.Redis(db=1)
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

    def parse_data(self, codes, dates, cookies, log_token, ck):
        temp_data = []
        for code in codes:
            for date in dates:
                try:
                    url = self.url + '?DCity1=' + code[0] + '&ACity1=' + code[1] + '&SearchType=S&DDate1=' + date + '&LogToken=' + log_token + '&CK=' + ck
                    cookies['FD_SearchHistorty'] = str(cookies['FD_SearchHistorty'])
                    response = requests.get(url, headers=self.headers, cookies=cookies)
                    time.sleep(random.random()*2+1)
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
                        self.rd2.rpush(self.collect_time, temp)
                except Exception as e:
                    code = response.content.decode(encoding='gb18030')
                    self.rd2.rpush('error', {url: str(e), 'error': str(code)})
                    break

    def run(self):
        datas = self.rd.lrange("xc_airport", 0, -1)
        data = json.loads(datas[0].decode().replace("'{", "{").replace("}'", "}").replace("'", "\""))
        dates = data['date']
        airports = data['airports']
        codes = []
        for airport in airports:
            codes.append(airport['code'])
        codes = self.parse_code(codes)
        cookies = data['cookie']
        params = data['param']
        log_token = params['log_token']
        ck = params['ck']
        self.parse_data(codes, dates, cookies, log_token, ck)

if __name__ == '__main__':
    url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights'
    xc = XiechengTicket(url)
    xc.run()
