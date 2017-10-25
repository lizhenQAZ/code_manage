"""all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# 引入首页视图函数
from . import views
# 引入配置文件
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),  # 首页
    url(r'^news/', include("news.urls", namespace="news")),  # 新闻页面
    url(r'^model/', include("model.urls", namespace="model")),  # 模型页面
    url(r'^view/', include("view.urls", namespace="view")),  # 视图页面
    url(r'^tpl/', include("tpl.urls", namespace="tpl")),  # 模板视图
    url(r'^deploy/', include('deploy.urls', namespace='deploy')),  # 部署视图
    # # 生产环境下设置静态文件查找方式
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]

# 匹配错误视图，不匹配返回默认处理页面
# handler404 = 'view.views.handle404'
# handler500 = 'view.views.handle500'
# handler403 = 'view.views.handle403'
