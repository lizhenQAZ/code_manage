# -*- coding: utf-8 -*-
from ..models import Post, Category
from django import template
register = template.Library()


# 最新文章模板
@register.simple_tag
def get_recent_posts(num=5):

    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板
@register.simple_tag
def archives():

    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板
@register.simple_tag
def get_categories():

    return Category.objects.all()
