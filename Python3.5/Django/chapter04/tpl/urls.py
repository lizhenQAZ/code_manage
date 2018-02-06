from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forstate/$', views.forstate),  # for控制语句
    url(r'^ifstate/$', views.ifstate),  # if控制语句
    url(r'^logicaloperator/$', views.logicaloperator),  # 逻辑操作符
    url(r'^collectionsoperator/$', views.collectionsoperator),  # 集合操作符
    url(r'^arithmeticoperator/$', views.arithmeticoperator),  # 算术操作符
    url(r'^myfilter/$', views.myfilter),  # 过滤器
    url(r'^mycomment/$', views.mycomment),  # 注释
    url(r'^tplinherit/$', views.tplinherit),  # 模板继承
    url(r'^htmlescape/$', views.htmlescape),  # html转义
    url(r'^message/$', views.message),  # 留言板功能
    url(r'register/$', views.register),  # 注册功能
    url(r'verificationcode/\d+/$', views.verificationcode),  # 验证码功能
]
