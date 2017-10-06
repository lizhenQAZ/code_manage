# 字典的遍历和修改不能同时操作
# 字典和集合的查询速度都很快

# dict
# 判断字典类型
# python3.5 不支持
# import abc
# print(isinstance({}, abc.Mapping))

# 创建字典
# 方式一
a = {'one': 1, 'two': 2, 'three': 3}
print(a)
# 方式二
a = dict(one=1, two=2, three=3)
print(a)
# 方式三
a = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(a)
# 方式四
a = dict([('one', 1), ('two', 2), ('three', 3)])
print(a)
# 方式五
a = dict({'one': 1, 'two': 2, 'three': 3})
print(a)

# 字典推导式
b = [('one', 1), ('two', 2), ('three', 3)]
print({eng: num for eng, num in b})
print({eng.upper(): num for eng, num in b})

# 字典查找插入新值
c = {}
test = [('four', 4), ('five', 5)]
for key, value in test:
    c.setdefault(key, []).append(value)
print(c)

# 字典查找取值
# 方式一
import collections
c = collections.defaultdict(list)
test = [('four', 4), ('five', 5)]
for key, value in test:
    print(c[key])  # []
# 方式二
test = {}
print(test.get('three', 'N/A'))  # ’N/A‘
# 方式三
print('three' in test)  # false

# 字典查询计数
# 统计字母个数
ct = collections.Counter("asdfgsfytyssncc")
print(ct)
# 增加统计的字母
ct.update("cnjjasbhcbds")
print(ct)
# 统计个数靠前的字母
print(ct.most_common(2))

# 只读的字典
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d[2] = 'B'
print(d_proxy)

# set
# 创造集合
print(frozenset(range(10)))

# 集合推导式
from unicodedata import name
print({chr(i) for i in range(35, 255) if 'SIGN' in name(chr(i), '')})

# 去重
l = ['apple', 'banana', 'apple', 'grape']
print(set(l))

# 求交集
# 方式一
set1 = {1, 3, 5, 7, 9, 10}
set2 = {2, 4, 6, 8, 10}
print(set1 & set2)
# 方式二
print(set(set1) & set(set2))
# 方式三
print(set(set1).intersection(set2))
