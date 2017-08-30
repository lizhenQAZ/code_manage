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
            title = bsobj.body.div.table
        except AttributeError as e:
            return None
        else:
            return title


# 获取img标签下属性src的链接地址的直接获取属性
title_list = gettitle(url)
print(title_list.attrs['id'])
