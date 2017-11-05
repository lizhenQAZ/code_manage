from django.db import models
from db.AbstractModel import AbstractModel
from django.contrib.auth.models import User


class Category(AbstractModel):
    # 文章分类
    name = models.CharField(max_length=100, verbose_name='分类名')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['-created_time']


class Tag(AbstractModel):
    # 文章标签
    name = models.CharField(max_length=100, verbose_name='标签名')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['-created_time']


class PostManager(models.Manager):
    pass


class Post(AbstractModel):
    # 文章标题
    title = models.CharField(max_length=70, verbose_name='标题')
    # 文章主体
    body = models.TextField(verbose_name='主要内容')
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    # 添加表关联
    # 文章类别
    cag = models.ForeignKey(Category, verbose_name='关联分类名')
    # 文章标签
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='关联标签名')
    # 文章作者
    author = models.ForeignKey(User, verbose_name='关联作者名')

    def __unicode__(self):
        return self.title

    objects = PostManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_time']
