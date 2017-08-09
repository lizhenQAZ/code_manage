from gevent import monkey
import gevent
import urllib.request
import multiprocessing
import re


# 有耗时操作时添加
monkey.patch_all()
url_list = list()


def load_html(url_info, q):
    print('url is: %s' % url_info)
    que = q
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read().decode('utf-8')
    content = re.findall(r'(https://[^>|^<]+\.jpg)', html_info)
    for j, pic_info in enumerate(content):
        que.put(pic_info)
        print(j, pic_info)


def download_jpg(file, url_info):
    print(url_info)
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read()
    with open(file, 'wb') as f:
        f.write(html_info)


def download_coroutine(q):
    que = q
    # print('url is %s' % url)
    for j in range(0, 10):
        if not que.empty():
            url_value = que.pop()
            filename = url_value
            g = gevent.spawn(download_jpg, filename, url_value)
            g.join()
        else:
            break


if __name__ == '__main__':
    url = '''https://www.douyu.com/directory/game/ecy'''
    queue = multiprocessing.Manager().Queue()
    load_html(url, queue)
    pool = multiprocessing.Pool(3)
    print('jdbvhybsfyvy')
    for i in range(0, 10):
        pool.apply_async(download_coroutine, args=(queue,))
    pool.close()
    # pool.join()
    print('finish')