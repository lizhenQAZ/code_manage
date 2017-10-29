#coding:utf-8
import requests
# 构建一个url
url = 'http://www.renren.com/PLogin.do'
# 构建请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

# 构建post数据
post_data = {
    "email": "17173805860",
    "password": "1qaz@WSX3edc"
}

# 创建session实例
session = requests.session()

# 发送post请求，模拟登陆
response = session.post(url,data=post_data,headers=headers)

print (response.url)
response1 = session.get('http://www.renren.com/923768535')
print (response1.url)
