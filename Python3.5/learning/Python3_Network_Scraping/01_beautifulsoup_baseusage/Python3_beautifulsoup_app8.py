from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


url = 'http://www.pythonscraping.com/pages/page3.html'
rex = re.compile('\.\./img/gifts/img.*\.jpg')


def gettitle(url_info):
    try:
        html = urlopen(url_info)
    except HTTPError as e:
        return None
    else:
        try:
            bsobj = BeautifulSoup(html.read())
            title = bsobj.find_all('img', {'src': rex})
        except AttributeError as e:
            return None
        else:
            return title


# 获取img标签下属性src的链接地址的正则表达式
title_list = gettitle(url)
for title_info in title_list:
    if title_info == None:
        print('Title could not be found')
    else:
        print(title_info['src'])
