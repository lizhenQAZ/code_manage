import urllib.request

# urlopen
print('*'*100)
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print('urlopen请求的结果: ', html)
# request
print('*'*100)
request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
html = response.read().decode()
print('request请求的结果: ', html)
# user-agent
print('*'*100)
url = 'http://www.itcast.cn'
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib.request.Request(url, headers=ua_header)
response = urllib.request.urlopen(request)
html = response.read()
print('user-agent请求的结果: ', html)
# 增加header
print('*'*100)
url = 'http://www.itcast.cn'
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib.request.Request(url, headers=header)
request.add_header("Connection", 'keep-alive')
response = urllib.request.urlopen(request)
print('增加header请求的响应码: ', response.code)
html = response.read().decode()
print('增加header请求的结果: ', html)
# 随机增加修改user_agent
import random
print('*'*100)
url = 'http://www.itcast.cn'
ua_list = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
]
user_agent = random.choice(ua_list)
request = urllib.request.Request(url)
request.add_header('User-Agent', user_agent)
print('增加user-agent请求的代理人: ', request.get_header('User-agent'))
response = urllib.request.urlopen(request)
html = response.read()
print('增加user_agent请求的结果: ', html)
