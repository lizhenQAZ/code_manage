# array存储浮点型数据
from array import array
from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])

# 数组排序
a = array('d', (11.5, 9.3, 12.1))
a = array(a.typecode, sorted(a))
print(a)

# 内存视图
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
# 转化成列表
print(memv.tolist())
print(len(memv))
# 转化成二进制
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 2
print(memv_oct.cast('h').tolist())
print(memv_oct.tolist())

