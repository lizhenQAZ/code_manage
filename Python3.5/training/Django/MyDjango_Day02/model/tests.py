from django.test import TestCase
from .models import *

import random

# 图书数据
book_list = ['射雕英雄传', '天龙八部', '笑傲江湖', '雪山飞狐']
# 创建测试数据
for book_name in book_list:
    # 创建图书对象
    book = BookInfo()
    # 字段赋值
    book.book_title = book_name
    book.book_comment = random.randint(1, 100)
    book.book_read = random.randint(1, 100)
    book.book_delete = False
    # 保存图书信息
    book.save()

# 英雄数据
hero_list = [
    {'name': '郭靖', 'sex': 1, 'desc': '降龙十八掌', 'book': 1},
    {'name': '黄蓉', 'sex': 0, 'desc': '打狗棍法', 'book': 1},
    {'name': '黄药师', 'sex': 1, 'desc': '弹指神通', 'book': 1},
    {'name': '欧阳锋', 'sex': 1, 'desc': '蛤蟆功', 'book': 1},
    {'name': '梅超风', 'sex': 0, 'desc': '九阴白骨爪', 'book': 1},
    {'name': '乔峰', 'sex': 1, 'desc': '降龙十八掌', 'book': 2},
    {'name': '段誉', 'sex': 1, 'desc': '六脉神剑', 'book': 2},
    {'name': '虚竹', 'sex': 1, 'desc': '天山六阳掌', 'book': 2},
    {'name': '王语嫣', 'sex': 0, 'desc': '神仙姐姐', 'book': 2},
    {'name': '令狐冲', 'sex': 1, 'desc': '独孤九剑', 'book': 3},
    {'name': '任盈盈', 'sex': 0,'desc': '弹琴', 'book': 3},
    {'name': '岳不群', 'sex': 1, 'desc': '华山剑法', 'book': 3},
    {'name': '东方不败', 'sex': 1, 'desc': '葵花宝典', 'book': 3},
    {'name': '胡斐', 'sex': 1, 'desc': '胡家刀法', 'book': 4},
    {'name': '苗若兰', 'sex': 0, 'desc': '黄衣', 'book': 4},
    {'name': '程灵素', 'sex': 0, 'desc': '医术', 'book': 4},
    {'name': '袁紫衣', 'sex': 0, 'desc': '六合拳', 'book': 4},
]

# 创建测试数据
for hero_info in hero_list:
    # 创建英雄类
    hero = HeroInfo()
    # 字段赋值
    hero.hero_name = hero_info['name']
    hero.hero_desc = hero_info['desc']
    hero.hero_sex = hero_info['sex']
    hero.hero_delete = False
    hero.hero_book_id = hero_info['book']
    # 保存对象
    hero.save()
