from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^book/$', query_book),  # 一对多查询
    url(r'^hero/$', query_hero),
    url(r'^place/$', query_place),  # 一对一查询
    url(r'^restaurant/$', query_restaurant),
    url(r'^dormitory/$', query_dormitory),  # 非级联删除
    url(r'^manager/$', query_manager),  # 自定义管理器类
    url(r'^queryset/$', query_set),  # 查询集
    url(r'^area/$', query_join),  # 自关联
    url(r'^order/$', order),  # 结果集排序(元选项定义排序方式)
    url(r'^bookmanage/$', query_bookmanage),  # 显示库存图书
    url(r'^logicaldelete/(\d+)/$', logicaldelete),  # 删除库存图书
]
