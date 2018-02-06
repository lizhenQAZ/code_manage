from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),  # 模板首页
    url(r'^dormitory/$', query_dormitory, name='dormitory'),  # 非级联删除
    url(r'^manager/$', query_manager, name='manager'),  # 自定义管理器类
    url(r'^queryset/$', query_set, name='queryset'),  # 查询集
    url(r'^area/$', query_join, name='area'),  # 自关联
    url(r'^order/$', order, name='order'),  # 结果集排序(元选项定义排序方式)
    # 一对多查询
    url(r'^book/$', query_book, name='book'),  # 单字段
    url(r'^hero/$', query_hero, name='hero'),  # 多字段
    # 一对一查询
    url(r'^place/$', query_place, name='place'),
    url(r'^restaurant/$', query_restaurant, name='restaurant'),
    # 图书管理
    url(r'^bookmanage/$', query_bookmanage, name='bookmanage'),  # 显示库存图书
    url(r'^logicaldelete/(\d+)/$', logicaldelete, name='logicaldelete'),  # 删除库存图书
]
