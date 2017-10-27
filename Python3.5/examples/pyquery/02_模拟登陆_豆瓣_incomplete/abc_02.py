import urllib.request
from pyquery import PyQuery as pq
import os


file = 'search.html'
if not os.path.isfile(file):
    url = "https://book.douban.com/"
    f = urllib.request.urlopen(url)
    print('---1---', f.info())
    print('---2---', f.geturl())
    print('---3---', f.getcode())
    with open(file, 'w', errors='ignore') as fp:
        fp.write(f.read().decode('utf-8'))

with open(file) as f:
    html = f.read()
    doc = pq(html)
    # print('---4---', doc)
    div = doc('div .hd ')
    print('---5---', div)
    # 迭代器
    span = div('span').filter(lambda i: pq(this)('a') == [])
    print('---6---', span.text())
