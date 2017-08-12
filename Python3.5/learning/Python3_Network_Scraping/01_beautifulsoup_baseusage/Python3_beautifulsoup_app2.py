from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


url = 'https://segmentfault.com/q/1010000006258352'


def gettitle(url_info):
    try:
        html = urlopen(url_info)
    except HTTPError as e:
        return None
    else:
        try:
            bsobj = BeautifulSoup(html.read())
            title = bsobj.body.h1
        except AttributeError as e:
            return None
        else:
            return title


# 读取h1标签下的内容，并处理url和tag不存在的异常
title_info = gettitle(url)
if title_info == None:
    print('Title could not be found')
else:
    print(title_info)