#coding:utf-8
import requests

# response = requests.get('http://www.baidu.com')
# 对cookies的转换
# print (response.cookies)
# print (type(response.cookies))

# 将cookiejar类型的cookies转换成python字典
# dict_cookie = requests.utils.dict_from_cookiejar(response.cookies)
# print (dict_cookie)
# print (type(dict_cookie))

# 将Python字典转换成cookiejar类型的数据
# jar_cookie = requests.utils.cookiejar_from_dict(dict_cookie)
# print (jar_cookie)
# print (type(jar_cookie))

# ssl认证
# url = 'https://www.12306.cn/mormhweb/'
# response = requests.get(url,verify=False)
# print (response.content)

# 超时设定
url = 'http://www.youtube.com'

response = requests.get(url,timeout=3)




