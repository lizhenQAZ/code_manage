# 拆包一
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print(city, year, pop, chg, area)

# 拆包二
travel_ids = [('USA', 125262), ('BRA', 156818), ('ESP', 484849)]
for passport in travel_ids:
    print("%s %s" % passport)

# 拆包三
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

# 交换值
a, b = 10, 20
a, b = b, a
print(a, b)

# 拆包四
import os
path, filename = os.path.split('/home/directory/test.txt')
print(path, filename)

# 拆包五
a, b, *rest = range(5)
print(a, b, rest)

# 拆包六
metro_areas = [('Tokyo', 'JP', 36.933, (12, 15))]
for city, province, code, (latitude, longitude) in metro_areas:
    print(city, province, code, latitude, longitude)

# 具名元组和字典的转化
from collections import  namedtuple
City = namedtuple('City', 'name country population latitude longtitude')
tokyo = City('Beijing', 'Haidian', 1750, 55, 78)
print(tokyo)
# 转化成字典
for key, value in tokyo._asdict().items():
    print(key + ": " + str(value))
