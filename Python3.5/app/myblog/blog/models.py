from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    # 文章摘要，可以没有文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 添加关系
    # 分类与标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
