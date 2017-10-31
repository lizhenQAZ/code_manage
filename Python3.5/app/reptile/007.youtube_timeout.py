# -*- coding: utf-8 -*
import requests


# 超时设定
url = 'http://www.youtube.com'
try:
    response = requests.get(url, timeout=3)
except Exception as e:
    print(e)
