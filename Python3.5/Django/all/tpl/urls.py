from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # tpl首页
    url(r'^forstate/$', views.forstate, name='forstate'),  # for控制语句
    url(r'^ifstate/$', views.ifstate, name='ifstate'),  # if控制语句
    url(r'^logicaloperator/$', views.logicaloperator, name='logicaloperator'),  # 逻辑操作符
    url(r'^collectionsoperator/$', views.collectionsoperator, name='collectionsoperator'),  # 集合操作符
    url(r'^arithmeticoperator/$', views.arithmeticoperator, name='arithmeticoperator'),  # 算术操作符
    url(r'^myfilter/$', views.myfilter, name='myfilter'),  # 过滤器
    url(r'^mycomment/$', views.mycomment, name='mycomment'),  # 注释
    url(r'^tplinherit/$', views.tplinherit, name='tplinherit'),  # 模板继承
    url(r'^htmlescape/$', views.htmlescape, name='htmlescape'),  # html转义
    url(r'^message/$', views.message, name='message'),  # 留言板功能
    url(r'register/$', views.register, name='register'),  # 注册功能
    url(r'verificationcode/(\d+)/$', views.verificationcode, name='verificationcode'),  # 验证码功能
]
