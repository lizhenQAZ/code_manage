import requests
from bs4 import BeautifulSoup
import os
import json


# 技术难点: 抓包和验证码、未知失败原因
user = os.environ.get('user')
password = os.environ.get('pwd')
print(user, password)
loginurl_get = 'https://www.zhihu.com/#signin'
loginurl = 'https://www.zhihu.com/login/phone_num'
centerurl = 'https://www.zhihu.com/settings/profile'

headers = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8'

}
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive'
# }

data = {
    'captcha_type': 'cn',
    'phone_num': user,
    'password': password
}

s = requests.session()
r = s.get(loginurl_get, headers=headers)
print(r.status_code)
with open('login.html', 'w') as f:
    f.write(r.text)

try:
    html = open('login.html', 'r')
except Exception as e:
    print(e)
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': '_xsrf'})['value']


data['_xsrf'] = token
print(token)
r_t = s.post(loginurl, data=json.dumps(data))
content = r_t.content.decode('utf-8')
print(r_t.url)
print(r_t.status_code)
print(r_t.cookies)
with open('index.html', 'w') as fp:
    fp.write(content)


r_t2 = s.get(centerurl)
content = r_t2.content.decode('utf-8')
print(r_t2.url)
print(r_t2.status_code)
print(r_t2.cookies)
with open('center.html', 'w', errors='ignore') as fp2:
    fp2.write(content)
