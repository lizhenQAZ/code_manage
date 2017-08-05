from gevent import monkey
import gevent
import urllib.request


#有耗时操作时添加
monkey.patch_all()


def download(filename, url):
    print('url is %s' % url)
    resp = urllib.request.urlopen(url)
    content = resp.read()
    with open(filename, 'wb') as f:
        f.write(content)


gevent.joinall([
    gevent.spawn(download, '1.jpg', 'https://imgsa.baidu.com/news/q%3D100/sign=3c363f11a9cc7cd9fc2d30d909002104/d058ccbf6c81800a8941adf2bb3533fa838b47a1.jpg'),
    gevent.spawn(download, '2.jpg', 'https://imgsa.baidu.com/news/q%3D100/sign=8d8768c464061d957b4633384bf50a5d/d62a6059252dd42a0cb21057093b5bb5c8eab896.jpg')
])
