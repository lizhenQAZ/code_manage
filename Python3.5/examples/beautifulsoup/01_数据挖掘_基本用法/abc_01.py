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
    print('---4---', soup.prettify())
    print('---5---', soup.title)
    print('---6---', soup.title.name)
    print('---7---', soup.title.string)
    print('---8---', soup.title.parent.name)
    print('---9---', soup.p)
    print('---10---', soup.p['class'])
    print('---11---', soup.a)
    print('---12---', soup.find_all('a'))
    print('---13---', soup.find(id='link3'))
    for link in soup.find_all('a'):
        print('---14---', link.get('href'))
    print('---15---', soup.get_text())
    print('---16---', soup.contents)
    print('---17---', soup.string)
    print('---18---', soup.name)
    print('---19---', len(list(soup.children)))
    print('---20---', len(list(soup.descendants)))
    for string in soup.strings:
        print('---21---', repr(string))
        print('---22---', string)
    for string in soup.stripped_strings:
        print('---23---', repr(string))
        print('---24---', string)
    print('---25---', soup.title.next_elements)
    print('---26---', soup.title.previous_elements)
    print('---27---', soup.title.next_sibling)
    print('---28---', soup.title.previous_sibling)
    print('---29---', soup.find_all(["a", "b"]))
    for tag in soup.find_all(True):
        print('---30---', tag.name)
        print('---31---', tag.has_attr('class'))
