# coding:utf-8
import requests
import re
# 构建一个url
url = 'http://www.renren.com/PLogin.do'
# 构建请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
# 构建post数据
post_data = {

}
# 创建session实例
session = requests.session()
# 发送post请求，模拟登陆
response = session.post(url, data=post_data, headers=headers)
print (response.url)
response1 = session.get('http://www.renren.com/960768847')
print (response1.url)
if re.findall(r'李震',response1.content.decode()):
    # 记录登录成功的页面
    with open('005_renren_session.html','wb')as f:
        f.write(response1.content)
else:
    print('not found!')
