# coding:utf-8
import requests
from lxml import etree
import re


# 构建一个url
login_url_get = 'https://github.com/login'
login_url_post = 'https://github.com/session'
target_url = 'https://github.com/settings/emails'
# 构建请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
# 构建post数据
post_data = {
    'commit': 'Sign in',
    'utf8':	'✓',
    # authenticity_token:
    # 'login':
    # 'password':
}
# 创建session实例
session = requests.session()
# 获取登录界面的提交信息
response_get = session.get(login_url_get, headers=headers, verify=False)
# print(response_get.url)
html = etree.HTML(response_get.content)
token = html.xpath('//input[@name="authenticity_token"]/@value')[0]
# print(token)
# # 拼接提交信息
user = input('请输入用户名: ')
pwd = input('请输入密码: ')
post_data['authenticity_token'] = token
post_data['login'] = user
post_data['password'] = pwd
# 发送post请求，模拟登陆
response_post = session.post(login_url_post, data=post_data)
print(response_post.url)
response_target = session.get(target_url)
print(response_target.url)
if re.findall(r'516960831@qq.com', response_target.content.decode()):
    # 记录登录成功的页面
    with open('020_github_login.html', 'wb')as f:
        f.write(response_target.content)
else:
    print('not found!')
