from django.test import TestCase
import random
# 导入模型类模块
from .models import *

# # 一对多查询
# # 单字段,图书数据
# books = ['射雕英雄传', '天龙八部', '笑傲江湖', '雪山飞狐']
# for book_name in books:
#     book = BookInfo()
#     book.book_title = book_name
#     book.book_comment = random.randint(1, 100)
#     book.book_read = random.randint(1, 100)
#     book.save()
#
# # 多字段,英雄数据
# heros = [
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
# for hero_info in heros:
#     hero = HeroInfo()
#     hero.hero_name = hero_info['name']
#     hero.hero_desc = hero_info['desc']
#     hero.hero_sex = hero_info['sex']
#     hero.hero_book_id = hero_info['book']
#     hero.save()

# 一对一查询
# 地点数据
# places = [
#     {'place_name': '上海市', 'place_address': '浦东新区航头镇', },
#     {'place_name': '南京市', 'place_address': '雨花台区铁心桥街道', },
# ]
# for place_info in places:
#     place = Place()
#     place.place_name = place_info['place_name']
#     place.place_address = place_info['place_address']
#     place.save()
#
# # 餐馆数据
# rests = [
#     {'rest_name': '肯德基', 'rest_place': 1, },
#     {'rest_name': '必胜客', 'rest_place': 2, },
# ]
# for rest in rests:
#     restaurant = Restaurant()
#     restaurant.rest_name = rest['rest_name']
#     restaurant.rest_place_id = rest['rest_place']
#     restaurant.save()


# # 非级联删除
# # 寝室数据
# dorms = [
#     {'dormitory_name': '205'},
#     {'dormitory_name': '401'},
# ]
# for dorm in dorms:
#     dormitory = Dormitory()
#     dormitory.dormitory_name = dorm['dormitory_name']
#     dormitory.save()
#
# # 人员数据
# members = [
#     {'member_name': '喜羊羊', 'member_dormitory': '1'},
#     {'member_name': '灰太狼', 'member_dormitory': '2'},
# ]
# for member_info in members:
#     member = Member()
#     member.member_name = member_info['member_name']
#     member.member_dormitory_id = member_info['member_dormitory']
#     member.save()


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
#     book.is_deleted = item[3]
#     book.save()

# # 自关联
# # 插入地区数据
# areas = [("北京", None),
#          ("河北", None),
#          ("海淀区", 1),
#          ("昌平区", 1),
#          ("顺义区", 1),
#          ("房山区", 1),
#          ("朝阳区", 1),
#          ("丰台区", 1),
#          ("石家庄", 2),
#          ("唐山", 2),
#          ("保定", 2),
#          ("邢台", 2),
#          ("邯郸", 2),
#          ("秦皇岛", 2)]
#
# for area in areas:
#     area_info = AreaInfo()
#     area_info.area_name = area[0]
#     area_info.area_parent_id = area[1]
#     area_info.save()
