from django.test import TestCase


from .models import *
from .data import *

# 插入地区数据
arealists = arealists

for arealist in arealists:
    area = AreaInfo()
    area.area_code = arealist[0]
    area.area_name = arealist[1]
    area.save()


# 插入省市区联动信息
city_info = city_info

for info in city_info:
    city = City()
    city.area_code = info[0]
    city.area_name = info[1]
    city.area_parent = info[2]
    city.save()
