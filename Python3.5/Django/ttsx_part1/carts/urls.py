#-*-coding:utf-8-*-


from django.conf.urls import url


from .views import *


urlpatterns = [
    url(r'^cart/$', cart, name='cart'),  # 后台管理
]
