# coding: utf-8
# 具名元组的属性和方法
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(City._fields)
print()
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
print()
for key, value in delhi._asdict().items():
    print(key + ':', value)
print()
