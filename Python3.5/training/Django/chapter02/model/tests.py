from django.test import TestCase

# 导入模型类模块
from .models import *
# 插入数据
import random

# # 图书数据
# book_list = ['射雕英雄传', '天龙八部', '笑傲江湖', '雪山飞狐']
# # 创建测试数据
# for book_name in book_list:
#     # 创建图书对象
#     book = BookInfo()
#     # 字段赋值
#     book.book_title = book_name
#     book.book_comment = random.randint(1, 100)
#     book.book_read = random.randint(1, 100)
#     book.book_delete = False
#     # 保存图书信息
#     book.save()
#
# # 英雄数据
# hero_list = [
#     {'name': '郭靖', 'sex': 1, 'desc': '降龙十八掌', 'book': 1},
#     {'name': '黄蓉', 'sex': 0, 'desc': '打狗棍法', 'book': 1},
#     {'name': '黄药师', 'sex': 1, 'desc': '弹指神通', 'book': 1},
#     {'name': '欧阳锋', 'sex': 1, 'desc': '蛤蟆功', 'book': 1},
#     {'name': '梅超风', 'sex': 0, 'desc': '九阴白骨爪', 'book': 1},
#     {'name': '乔峰', 'sex': 1, 'desc': '降龙十八掌', 'book': 2},
#     {'name': '段誉', 'sex': 1, 'desc': '六脉神剑', 'book': 2},
#     {'name': '虚竹', 'sex': 1, 'desc': '天山六阳掌', 'book': 2},
#     {'name': '王语嫣', 'sex': 0, 'desc': '神仙姐姐', 'book': 2},
#     {'name': '令狐冲', 'sex': 1, 'desc': '独孤九剑', 'book': 3},
#     {'name': '任盈盈', 'sex': 0,'desc': '弹琴', 'book': 3},
#     {'name': '岳不群', 'sex': 1, 'desc': '华山剑法', 'book': 3},
#     {'name': '东方不败', 'sex': 1, 'desc': '葵花宝典', 'book': 3},
#     {'name': '胡斐', 'sex': 1, 'desc': '胡家刀法', 'book': 4},
#     {'name': '苗若兰', 'sex': 0, 'desc': '黄衣', 'book': 4},
#     {'name': '程灵素', 'sex': 0, 'desc': '医术', 'book': 4},
#     {'name': '袁紫衣', 'sex': 0, 'desc': '六合拳', 'book': 4},
# ]
# # 创建测试数据
# for hero_info in hero_list:
#     # 创建英雄类
#     hero = HeroInfo()
#     # 字段赋值
#     hero.hero_name = hero_info['name']
#     hero.hero_desc = hero_info['desc']
#     hero.hero_sex = hero_info['sex']
#     hero.hero_delete = False
#     hero.hero_book_id = hero_info['book']
#     # 保存对象
#     hero.save()
#
# # 地点数据
# place_list = [
#     {'place_name': '上海市', 'place_address': '浦东新区航头镇', },
#     {'place_name': '南京市', 'place_address': '雨花台区铁心桥街道', },
# ]
# # 创建测试数据
# for place_info in place_list:
#     # 创建地点类
#     place = Place()
#     # 字段赋值
#     place.place_name = place_info['place_name']
#     place.place_address = place_info['place_address']
#     # 保存对象
#     place.save()
#
# # 餐馆数据
# res_list = [
#     {'res_name': '肯德基', 'res_place': 1, },
#     {'res_name': '必胜客', 'res_place': 2, },
# ]
# # 创建测试数据
# for res_info in res_list:
#     # 创建地点类
#     restaurant = Restaurant()
#     # 字段赋值
#     restaurant.res_name = res_info['res_name']
#     restaurant.res_place_id = res_info['res_place']
#     # 保存对象
#     restaurant.save()
#
# # 寝室数据
# dorm_list = [
#     {'dormitory_name': '205'},
#     {'dormitory_name': '401'},
# ]
# # 创建测试数据
# for dorm_info in dorm_list:
#     # 创建地点类
#     dormitory = Dormitory()
#     # 字段赋值
#     dormitory.dormitory_name = dorm_info['dormitory_name']
#     # 保存对象
#     dormitory.save()
#
# # 人员数据
# member_list = [
#     {'member_name': '喜羊羊', 'member_dormitory': '1'},
#     {'member_name': '灰太狼', 'member_dormitory': '2'},
# ]
# # 创建测试数据
# for member_info in member_list:
#     # 创建地点类
#     member = Member()
#     # 字段赋值
#     member.member_name = member_info['member_name']
#     member.member_dormitory_id = member_info['member_dormitory']
#     # 保存对象
#     member.save()
#
# # 新的图书数据
# book_list = [('射雕英雄传', 10, 10, True),
#              ('天龙八部', 20, 20, False),
#              ('笑傲江湖', 30, 30, True),
#              ('雪山飞狐', 40, 40, False), ]
#
# for item in book_list:
#     book = BookDesc()
#     book.book_title = item[0]
#     book.book_read = item[1]
#     book.book_comment = item[2]
#     book.book_isdelete = item[3]
#     book.save()

# 自关联
# 插入地区数据
areas = [("北京", None),
         ("河北", None),
         ("海淀区", 1),
         ("昌平区", 1),
         ("顺义区", 1),
         ("房山区", 1),
         ("朝阳区", 1),
         ("丰台区", 1),
         ("石家庄", 2),
         ("唐山", 2),
         ("保定", 2),
         ("邢台", 2),
         ("邯郸", 2),
         ("秦皇岛", 2)]

for area in areas:
    area_info = AreaInfo()
    area_info.area_name = area[0]
    area_info.area_parent_id = area[1]
    area_info.save()
