# coding:utf-8
import requests
from lxml import etree
import re


# 构建一个url
login_url_post = 'https://www.douban.com/login'
target_url = 'https://www.douban.com/accounts/'
# 构建请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
# 构建post数据
post_data = {
    # 'form_email':
    'redir': 'https://www.douban.com',
    # 'form_password':
    'source': 'None',
    'login': '登录',
}
# 创建session实例
session = requests.session()
# 拼接post请求
email = input('请输入用户名: ')
pwd = input('请输入密码: ')
post_data['form_email'] = email
post_data['form_password'] = pwd
# 发送post请求，模拟登陆
response_post = session.post(login_url_post, data=post_data, headers=headers, verify=False)
print(response_post.url)
response_target = session.get(target_url)
print(response_target.url)
if re.findall(r'516960831@qq.com', response_target.content.decode()):
    # 记录登录成功的页面
    with open('021_douban_login.html', 'wb')as f:
        f.write(response_target.content)
else:
    print('not found!')
