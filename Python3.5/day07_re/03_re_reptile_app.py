from gevent import monkey
import gevent
import urllib.request
from multiprocessing import Process, Queue
import re


# 有耗时操作时添加
monkey.patch_all()
url_list = list()


def load_html(url_info):
    print('url is: %s' % url_info)
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read().decode('utf-8')
    content = re.findall(r'(https://[^>|^<]+\.jpg)', html_info)
    for i, pic_info in enumerate(content):
        print(i, pic_info)
    return content


def download_jpg(file, url_info):
    print(url_info)
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read()
    with open(file, 'wb') as f:
        f.write(html_info)


def download(url_msg):
    url_info = url_msg
    # print('url is %s' % url)
    for file_no in range(1, len(url_info)+1):
        filename = 'meizi' + str(file_no) + '.jpg'
        print(file_no)
        g = gevent.spawn(download_jpg, filename, url_info[file_no-1])
        g.join()


if __name__ == '__main__':
    url = '''https://www.douyu.com/directory/game/ecy'''
    q = Queue(3)
    url_list = load_html(url)
    p = Process(target=download, args=(url_list,))
    p.start()