import requests
from bs4 import BeautifulSoup
import os


user = os.environ.get('login')
password = os.environ.get('password')
print(user, password)
loginurl_get = 'https://github.com/login'
loginurl = 'https://github.com/session'
marketurl = 'https://github.com/marketplace'

headers = {
    'Host': 'github.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'login': user,
    'password': password
}

r = requests.get(loginurl_get, headers=headers)
print(r.status_code)
# 每次请求cookies后需要重新设置cookies并且传入data、headers参数
cookies = r.cookies.get_dict()
print(cookies)
with open('login.html', 'w') as f:
    f.write(r.text)


try:
    html = open('login.html', 'r')
except Exception as e:
    print(e)
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'authenticity_token'})['value']


data['authenticity_token'] = token
r_t = requests.post(loginurl, headers=headers, data=data, cookies=cookies)
content = r_t.content.decode('utf-8')
print(r_t.url)
print(r_t.status_code)
cookies = r_t.cookies.get_dict()
print(cookies)
with open('index.html', 'w') as fp:
    fp.write(content)


r_t2 = requests.get(marketurl, headers=headers, cookies=cookies)
content = r_t2.content.decode('utf-8')
print(r_t2.url)
print(r_t2.status_code)
cookies = r_t2.cookies.get_dict()
print(cookies)
with open('market.html', 'w', errors='ignore') as fp2:
    fp2.write(content)
