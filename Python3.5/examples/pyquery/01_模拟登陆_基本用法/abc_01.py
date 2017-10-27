# from pyquery import PyQuery
# from lxml import etree
# import urllib
# from urllib.request import urlopen


"""==========================================="""
# d = PyQuery("<html></html>")
# print("---1---", d)
# d = PyQuery(etree.fromstring("<html></html>"))
# print("---2---", d)
#
# # 提取网页信息
# url = "https://www.baidu.com/"
# d = PyQuery(url=url)
# print("---3---", d)
#
# # 提取js信息
# your_url = "https://www.baidu.com/"
# d = PyQuery(url=your_url, opener=lambda url, **kw: urlopen(url).read())
# print("---4---", d)


"""==========================================="""
# 提取文件信息 ?
# d = PyQuery(filename="search.html")
# print("---5---", d)
# d_info = d("#hello")
# print("---6---", d_info)
# print("---7---", d_info.html())

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
# </div>
# '''
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# print("---8---", doc)
# print("---9---", type(doc))
# print("---10---", doc('li'))

# doc = pq(url="http://www.baidu.com", encoding='utf-8')
# 查询tag
# print("---11---", doc('head'))


"""==========================================="""
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# # 查询id、class、tag
# print(doc('---12---', '#container .list li'))


'''======================>子元素<======================='''
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print('---13---', type(items))
# print('---13---', items)
# lis = items.find('li')
# print('---13---', type(lis))
# print('---13---', lis)
# li = items.children()
# print('---13---', type(li))
# print('---13---', li)


'''======================>父元素<======================='''
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print('---14---', type(container))
# print('---14---', container)

# 查找所有父元素
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print('---14---', type(parents))
# print('---14---', parents)

"""=================================>兄弟元素<============================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print('---15---', li.siblings())


"""================================>单个元素<==============================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print('---16---', li)
#
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print('---16---', type(li))
#     print('---16---', li)


"""=========================>获取属性<================================"""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print('---17---', a)
# print('---17---', a.attr('href'))
# print('---17---', a.attr.href)


"""============================>获取文本<============================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print('---18---', a)
# print('---18---', a.text())


"""=======================>获取html<================================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print('---19---', li)
# print('---19---', li.html())


"""======================>addClass、removeClass<====================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print('---20---', li)
# li.removeClass('active')
# print('---20---', li)
# li.addClass('active')
# print('---20---', li)


"""===========================>attr、css<==========================="""
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print('---21---', li)
# li.attr('name', 'link')
# print('---21---', li)
# li.css('font-size', '14px')
# print('---21---', li)


"""===========================>remove<============================="""
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
print('---22---', wrap.text())
wrap.find('p').remove()
print('---22---', wrap.text())
