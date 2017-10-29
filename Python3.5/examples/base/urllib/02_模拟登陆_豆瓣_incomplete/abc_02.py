import urllib.request


url = "https://book.douban.com/"
f = urllib.request.urlopen(url)
print('---1---', f.info())
print('---2---', f.geturl())
print('---3---', f.getcode())
with open('search.html', 'w', errors='ignore') as fp:
    fp.write(f.read().decode('utf-8'))
