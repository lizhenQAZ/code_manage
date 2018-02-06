# coding: utf-8
# 使用具名元祖
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print()
print(tokyo.population, end='\r\n')
print()
print(tokyo.coordinates, end='\r\n')
print()
print(tokyo[1], end='\r\n')
print()
