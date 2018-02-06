# coding: utf-8
from functools import reduce
from operator import add
# reduce累加
print(reduce(add, range(100)))
print(sum(range(100)))
