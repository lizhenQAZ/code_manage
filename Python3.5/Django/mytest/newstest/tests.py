from django.test import TestCase


# 引入模型类模块
from .models import *


# # 1. 插入数据
# # 创建分类对象
# news_cag = NewsCag()
# news_cag.cag_name = '军事新闻'
# # 调用模型类的save方法,即可向数据库中添加此方法
# news_cag.save()
#
# # 创建一条新闻信息对象
# news_info = NewsInfo()
# news_info.news_title = "中国8艘核动力航母已部署到太平洋地区"
# news_info.news_content = "据新华社报道, 中国8艘核动力航母已部署到太平洋地区，随时准备和美国对抗,将美军赶出亚太地区."
# news_info.news_cag = news_cag
# news_info.save()


# # 2. 修改数据
# # 根据ID先获得数据信息
# news_info = NewsInfo.objects.get(id=1)
# print(news_info)
#
# news_info.news_title = '修改为新标题'
# news_info.save()


# # 3. 查询数据
# # 获得所有新闻信息数据
# news_list = NewsInfo.objects.all()
# # 获取某条数据
# news_info = NewsInfo.objects.get(pk=1)
# print(news_info.news_title)
# print(news_info.news_cag)
# print(news_info.news_content)


# # 4. 删除数据
# news_info = NewsInfo.objects.get(pk=1)
# news_info.delete()
