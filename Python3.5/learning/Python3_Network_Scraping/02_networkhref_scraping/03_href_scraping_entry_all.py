from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())
url_root = 'https://en.wikipedia.org'
first_link = '/wiki/Kevin_Bacon'
rex = re.compile('^(/wiki/)((?!:).)*$')


def gettitle(url_info):
    try:
        html = urlopen(url_root + url_info)
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


# 获取a标签下词条属性href的所有链接地址
title_list = gettitle(first_link)
while len(title_list) > 0:
    new_link = title_list[random.randint(0, len(title_list)-1)].attrs['href']
    print(new_link)
    title_list = gettitle(new_link)