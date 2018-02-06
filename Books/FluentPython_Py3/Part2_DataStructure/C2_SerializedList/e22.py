# coding: utf-8
# 高阶数组操作
import numpy
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
print()
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
a.transpose()
print(a)
