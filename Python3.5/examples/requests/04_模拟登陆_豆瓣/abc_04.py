import requests
from bs4 import BeautifulSoup
import os


user = os.environ.get('login')
password = os.environ.get('pwd')
print(user, password)
loginurl_get = 'https://www.douban.com/login'
loginurl = 'https://accounts.douban.com/login'
centerurl = 'https://www.douban.com/accounts/'

headers = {
    'Host': 'www.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
}

data = {
    'form_email': user,
    'form_password': password,
    'remember': 'on',
    'login': '登录'
}

s = requests.session()
r = s.get(loginurl_get, headers=headers)
print(r.status_code)
with open('login.html', 'w') as f:
    f.write(r.text)


r_t = s.post(loginurl, data=data)
content = r_t.content.decode('utf-8')
print(r_t.url)
print(r_t.status_code)
print(r_t.cookies)
with open('index.html', 'w', errors='ignore') as fp:
    fp.write(content)


r_t2 = s.get(centerurl)
content = r_t2.content.decode('utf-8')
print(r_t2.url)
print(r_t2.status_code)
print(r_t2.cookies)
with open('center.html', 'w', errors='ignore') as fp2:
    fp2.write(content)
