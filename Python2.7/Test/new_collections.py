#!usr/bin/python
# -*- coding:utf-8 -*-

#collections.namedtupule
'''
from collections import namedtuple
websites=[("sohu","http://www.google.com/","张朝阳"),("sina","http://www.sina.com/","王志东"),("163","http://www.163.com/","丁磊")]
Website=namedtuple('website',['name','url',u'founder'])
for website in websites:
    website=Website._make(website)
    print website
'''

#collections.deque
"""
import sys
import time
from collections import deque

deques=deque(">....................")
while True:
    deques.rotate(1)
    sys.stdout.flush()
    time.sleep(0.5)
    print deques
"""

#collections.Counter
'''
from collections import Counter

s="I am not a clever boy,but I am well diligent"
c=Counter(s)
print c.most_common(5)

#collections.OrderedDict
from collections import OrderedDict

item=(('A',1),('B',2),('C',3))
s=dict(item)
os=OrderedDict(item)
print s,os
for k,v in s.items():
    print k,v,'\t',
print '\n'
for k,v in os.items():
    print k, v, '\t',
'''

#collections.defaultdict
from collections import defaultdict
dict={'A':1}
dict=defaultdict(lambda:"N/A")
print dict['A']
print dict['key1']