from django.test import TestCase


# 引入模型类
from .models import *


# 1. 插入数据
news_cag = NewsCategory()
news_cag.cag_name = "体育新闻"
news_cag.save()

news_info = NewsInfo()
news_info.news_title = "国际新闻"
news_info.news_content = "千年虫"
news_info.news_cag = news_cag
news_info.save()


# 2.读取数据
# 获取指定信息
news_infos = NewsInfo.objects.all()
for news_info in news_infos:
    print(news_info.news_title)


# 获取某个信息
news_1 = NewsInfo.objects.get(id=2)
print(news_1.news_title)


# 3.修改数据
news_1 = NewsInfo.objects.get(pk=2)
news_1.news_title = "科技新闻"
news_1.save()
print(news_1.news_title)

# 4.删除数据
news_1 = NewsInfo.objects.get(pk=2)
news_1.delete()
print(news_1.news_title)
