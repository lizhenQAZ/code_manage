from gevent import monkey
import gevent
import urllib.request


#有耗时操作时添加
monkey.patch_all()


def download(url):
    print('url is %s' % url)
    resp = urllib.request.urlopen(url)
    content = resp.read()
    print('%d bytes received from %s.' % (len(content), url))


gevent.joinall([
    gevent.spawn(download, 'http://www.baidu.com/'),
    gevent.spawn(download, 'http://www.itcast.cn/')
])