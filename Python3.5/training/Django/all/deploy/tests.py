from django.test import TestCase
# 自定义模型类
from .models import *
# 数据文件类
from .data import *

# # 插入地区数据
# areas = arealists
# for areainfo in areas:
#     area = AreaInfo()
#     area.area_code = areainfo[0]
#     area.area_name = areainfo[1]
#     area.save()

# 插入省市区联动信息
# city_info = city_info
# for info in city_info:
#     city = City()
#     city.area_code = info[0]
#     city.area_name = info[1]
#     city.area_parent = info[2]
#     city.save()
