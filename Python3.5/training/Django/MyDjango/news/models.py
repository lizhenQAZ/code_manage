from django.db import models


# 定义新闻分类表
class NewsCategory(models.Model):
    # 定义新闻分类名称
    cag_name = models.CharField(max_length=50)


# 定义新闻信息表
class NewsInfo(models.Model):
    # 定义新闻标题
    news_title = models.CharField(max_length=50)
    # 定义新闻内容
    news_content = models.TextField()
    # 定义新闻扥类
    news_cag = models.ForeignKey('NewsCategory')
