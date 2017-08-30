from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


url_root = 'https://en.wikipedia.org'
first_link = ''
rex = re.compile('^(/wiki/)')
url_list = list()


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
            for url_msg in title:
                if 'href' in url_msg.attrs:
                    new_url = url_msg.attrs['href']
                    if new_url not in url_list:
                        url_list.append(new_url)
                        print(new_url)
                        gettitle(new_url)


# 获取a标签下词条属性href的所有链接地址,并记录在列表里
gettitle(first_link)