#-*-coding:utf-8-*-


from django.conf.urls import url


from .views import *


urlpatterns = [
    url(r'^index/$', index, name='index'),  # 商品首页
    url(r'^goods_list/$', goods_list, name='goods_list'),  # 商品列表
    url(r'^detail/$', detail, name='detail'),  # 商品详情
]
