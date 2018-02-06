from django.db import models
# 引入公共模型类
from db.AbstractModel import AbstractModel


# 创建新闻分类表
class NewsCategory(AbstractModel):
    cag_name = models.CharField(max_length=50)


# 创建新闻信息表
class NewsInfo(AbstractModel):
    news_title = models.CharField(max_length=50)
    news_content = models.CharField(max_length=5000)
    news_category = models.ForeignKey(NewsCategory)
