#coding:utf-8
import requests

# 构建url
url = 'http://www.sina.com.cn/'
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
# 发起请求
response = requests.get(url, headers=headers)
# 验证text
# print (response.text)
# 验证content.decode（）
print(response.content.decode())
