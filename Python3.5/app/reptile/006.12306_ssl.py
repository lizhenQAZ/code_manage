# coding:utf-8
import requests


# ssl认证
url = 'https://www.12306.cn/mormhweb/'
response = requests.get(url, verify=False)
print (response.content)
