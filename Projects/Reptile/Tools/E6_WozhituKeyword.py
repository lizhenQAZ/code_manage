# coding: utf-8
import requests
import json

url = 'http://api1.wozhitu.com:8080/imagesearch/api/v1.0/kwdsuggest'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

data = {
    'apikey': '',
    'imgFile':  open('G:/1.jpg'),
    'clientname': '',
    'kwdtopnum': '10',
    'subjectKwd': ''
}

response = requests.post(url, headers=headers, data=data)
print(response.content)
data = json.loads(response.content)
print(data['topKwd'])
