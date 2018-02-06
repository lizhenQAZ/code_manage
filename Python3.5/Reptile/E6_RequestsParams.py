#coding:utf-8

import requests

# 构建一个url
url = 'https://www.baidu.com/s'
# 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
# 构建请求参数
params = {
    "wd": "python",
}


# 发送请求
response = requests.get(url, headers=headers, params=params)

with open('baidu.html', 'wb')as f:
    f.write(response.content)
