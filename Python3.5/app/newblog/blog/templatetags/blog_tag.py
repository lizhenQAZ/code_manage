# coding: utf-8
from django import template
from ..models import Post, Category
register = template.Library()


# 最新文章
@register.simple_tag
def post_by_new_five(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def post_by_dates():
    return Post.objects.datetimes('created_time', 'day', order='DESC')


# 分类
@register.simple_tag
def category_all():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
