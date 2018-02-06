#coding:utf-8

# 导入库
import requests

# 构建一个url(url需要有协议)
url = 'https://www.baidu.com'
# 发起请求
response = requests.head(url)

# 状态码
# print(response.status_code)

# 响应的url
# print(response.url)

# 查看请求头
# print(response.request.headers)

# 查看响应头
print(response.headers)

# 查看二进制源码
# print(response.content.decode())

# 查看str类型的源码
# print(response.encoding)
# response.encoding='utf-8'
# print(response.text)
