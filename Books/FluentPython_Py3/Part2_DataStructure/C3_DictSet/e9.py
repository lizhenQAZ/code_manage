# coding: utf-8
# 不可变映射类型
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = 'x'
except TypeError as e:
    print(e)
print()
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])
