from gevent import monkey
import gevent
import urllib.request
import multiprocessing
import re
import threading


# 有耗时操作时添加
monkey.patch_all()
url_list = list()


def load_html(url_info, q):
    print('url is: %s' % url_info)
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read().decode('utf-8')
    content = re.findall(r'(https://[^>|^<]+\.jpg)', html_info)
    for j, pic_info in enumerate(content):
        q.put(pic_info)
        print(j, pic_info)


def download_jpg(file, url_info):
    print(url_info)
    resp = urllib.request.urlopen(url_info)
    html_info = resp.read()
    with open(file, 'wb') as f:
        f.write(html_info)


def download_thread(q, files_num):
    mutex = threading.Lock()
    que = q
    # print('url is %s' % url)
    for j in range(0, 10):
        threading.Thread(target=download_coroutine, args=(q, files_num, mutex))
        threading.start()


def download_coroutine(q, files_num, mutex):
    que = q
    # print('url is %s' % url)
    for j in range(0, 10):
        flag = mutex.acquire()
        if flag:
            if not que.empty():
                url_value = que.pop()
                file_no = files_num - que.qsize()
                print(file_no)
                filename = 'meizi' + str(file_no) + '.jpg'
                g = gevent.spawn(download_jpg, filename, url_value)
                g.join()
            else:
                break
            mutex.release()


if __name__ == '__main__':
    url = '''https://www.douyu.com/directory/game/ecy'''
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(3)
    load_html(url, queue)
    all_files_num = len(queue.qsize())
    for i in range(0, 10):
        pool.apply_async(download_thread, args=(queue, all_files_num))
    pool.close()
    pool.join()
    print('finish')