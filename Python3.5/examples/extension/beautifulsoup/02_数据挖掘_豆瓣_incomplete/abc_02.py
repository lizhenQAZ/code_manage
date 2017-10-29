import urllib.request
from bs4 import BeautifulSoup
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
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', attrs={'class': "hd"}):
        # if item.has_attr('class') and not item.has_attr('href'):
        # if item.string == '新书速递':
        # print(div)
        for item in div.find_all('span', {'class': ''}):
            print(item.string)
