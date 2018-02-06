# coding: utf-8
from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()


# 最新文章
@register.simple_tag
def post_by_new_five(num=5):
    return Post.objects.all()[:num]


# 归档
@register.simple_tag
def post_by_dates():
    return Post.objects.datetimes('created_time', 'day', order='DESC')


# 分类
@register.simple_tag
def category_all():
    # 别忘了在顶部引入 Category 类
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


# 标签
@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
