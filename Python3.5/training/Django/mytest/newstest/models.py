from django.db import models


# 定义新闻分类表
class NewsCag(models.Model):  # 注意模型类必须继承自models.Model类
    # 定义分类名称属性
    cag_name = models.CharField(max_length=50)


# 定义新闻信息类
class NewsInfo(models.Model):
    # 定义新闻标题
    news_title = models.CharField(max_length=50)
    # 定义新闻内容
    news_content = models.TextField(max_length=5000)
    # 定义新闻分类
    news_cag = models.ForeignKey('NewsCag')
