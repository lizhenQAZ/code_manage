import requests

# 直接调用get方法
print('*'*100)
response = requests.get('http://www.baidu.com')
print("get请求的结果: ", response)
# 添加headers和查询参数
print('*'*100)
kw = {'wd', '上海'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get('http://www.baidu.com/', params=kw, headers=headers)
print('get请求unicode格式数据: ', response.text)
print('get请求二进制格式数据: ', response.content)
print('get请求完整的url: ', response.url)
print('get请求头部字节编码: ', response.encoding)
print('get请求响应码: ', response.status_code)
# 获取新浪首页
print('*'*100)
response = requests.get('http://www.sina.com')
print('get请求头: ', response.request.headers)
# print('get请求内容猜测解压功能: ', response.text.decode())
# print('get请求内容自带解压功能: ', response.content.decode())
# 获取 网络上图片的大小
from io import BytesIO, StringIO
from PIL import Image
img_url = "http://imglf1.ph.126.net/pWRxzh6FRrG2qVL3JBvrDg==/6630172763234505196.png"
response = requests.get(img_url)
f = BytesIO(response.content)
img = Image.open(f)
print(img.size)

