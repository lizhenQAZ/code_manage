#coding:utf-8

import requests

# 构建一个url
url = 'http://www.toutiao.com'
# 构建一个请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

# 构建代理
# proxies ={
#     "http": "http://203.122.220.239:8080",
#     "https": "https://203.122.220.239:8080",
# }
proxies ={
    "http": "http://morganna_mode_g:ggc22qxp@120.24.171.107:16816",
    "https": "https://morganna_mode_g:ggc22qxp@120.24.171.107:16816",
}

# 发送请求获取响应
response = requests.get(url,headers=headers,proxies=proxies)

# ？如何判断代理使用正常
print(response.headers)
with open('2_request_proxies.html', 'w') as f:
    f.write(response.content.decode())
