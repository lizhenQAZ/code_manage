from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
rex = re.compile('^(/wiki/)((?!:).)*$')


def gettitle(url_info):
    try:
        html = urlopen(url_info)
    except HTTPError as e:
        return None
    else:
        try:
            bsobj = BeautifulSoup(html.read())
            title = bsobj.find('div', {'id': 'bodyContent'}).find_all('a', {'href': rex})
        except AttributeError as e:
            return None
        else:
            return title


# 获取a标签下词条属性href的链接地址
title_list = gettitle(url)
for title_info in title_list:
    if 'href' in title_info.attrs:
        print(title_info.attrs['href'])
