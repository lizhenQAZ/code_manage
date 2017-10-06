import numpy

# 创建数组
a = numpy.arange(12)
print(a)

# 判断数组类型
print(type(a))

# 改变数组的维数
a.shape = 3, 4
print(a)

# 取第三行
print(a[2])

# 取元素
print(a[2, 1])

# 取第二列
print(a[:, 1])

# 数组转置
print(a.transpose())