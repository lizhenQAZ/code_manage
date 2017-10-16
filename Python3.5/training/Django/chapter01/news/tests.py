from django.test import TestCase


# 引入模型类模块
from .models import *


# 1.插入数据
# 创建新闻分类对象
news_cag = NewsCategory()
news_cag.cag_name = '军事新闻'
news_cag.save()

# 创建新闻信息对象
news_info = NewsInfo()
news_info.news_title = "大战一触即发"
news_info.news_content = "这是一个假新闻"
news_info.news_category = news_cag
news_info.save()


# # 2.修改数据
# # 获取数据并且修改
# news_info = NewsInfo.objects.get(id=1)
# print(news_info)
# news_info.news_title = "国际新闻"
# news_info.save()


# # 3.查询数据
# # 查询所有数据
# news_info = NewsInfo.objects.all()
# for index, item in enumerate(news_info):
#     print(index, " 新闻标题: ", item.news_title, ' 新闻内容: ', item.news_content)
# news_info = NewsInfo.objects.get(pk=1)
# print("新闻标题: ", news_info.news_title, ' 新闻内容: ', news_info.news_content)


# 4.删除数据
# news_info = NewsInfo.objects.get(pk=1)
# news_info.delete()
print('新闻信息对象: ', NewsInfo.objects.all())
