# -*- coding: utf-8 -*-
import requests
'''
网络爬虫之用户名密码及验证码登陆：爬取知乎网站
'''


def create_session():
    login_data = {
        # 'redir': 'https://www.douban.com',
        'form_email': '516960831@qq.com',
        'form_password': 'lz211314'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host': 'www.douban.com',
        # 'Origin': 'https://www.douban.com',
        # 'Referer': 'https://www.douban.com/accounts/login?redir=https%3A//www.douban.com/mine/'
    }

    session = requests.session()
    r = session.post('https://accounts.douban.com/login', data=login_data, headers=headers)
    print(r)
    print(r.cookies)
    with open('post.html', 'w', encoding='utf-8') as fp:
        fp.write(r.content.decode('utf-8'))


if __name__ == '__main__':
    create_session()
