from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


url = 'http://www.pythonscraping.com/pages/page3.html'


def gettitle(url_info):
    try:
        html = urlopen(url_info)
    except HTTPError as e:
        return None
    else:
        try:
            bsobj = BeautifulSoup(html.read())
            title = bsobj.find('table', {'id': 'giftList'}).children
        except AttributeError as e:
            return None
        else:
            return title


# 获取table标签下属性id为giftList的内容的所有子标签
title_list = gettitle(url)
for title_info in title_list:
    if title_info == None:
        print('Title could not be found')
    else:
        print(title_info)