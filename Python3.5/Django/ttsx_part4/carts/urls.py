#-*-coding:utf-8-*-
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^cart/$', cart, name='cart'),  # 购物车首页
    url(r'^add_carts/$', add_carts, name='add_carts'),  # 商品加入购物车
]
