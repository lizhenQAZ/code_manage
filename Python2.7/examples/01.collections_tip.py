#!usr/bin/python
# -*- coding:utf-8 -*-
import sys
import time
from collections import *

# collections.namedtupule
# websites = [
#     ("sohu", "http://www.google.com/", "张朝阳"),
#     ("sina", "http://www.sina.com/", "王志东"),
#     ("163", "http://www.163.com/", "丁磊"),
# ]
# Website = namedtuple('website', ['name', 'url', u'founder'])
# for website in websites:
#     website = Website._make(website)
#     print website
#
# # collections.deque
# deques = deque(">....................")
# while True:
#     deques.rotate(1)
#     sys.stdout.flush()
#     time.sleep(0.5)
#     print deques

# # collections.Counter
# s = "I am not a clever boy,but I am well diligent"
# c = Counter(s)
# print c.most_common(5)

# # collections.OrderedDict
# item = (('A', 1), ('B', 2), ('C', 3))
# s = dict(item)
# os = OrderedDict(item)
# print '*'*100
# print s, '\n', os
# print '*'*100
# for k, v in s.items():
#     print k, v, '\t'
# print '*'*100
# for k, v in os.items():
#     print k, v, '\t'

# # collections.defaultdict
# dict = {'A': 1}
# dict = defaultdict(lambda: "N/A")
# print dict['A']
# print dict['key1']
