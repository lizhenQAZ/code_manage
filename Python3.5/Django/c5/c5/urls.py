"""chapter05 URL Configuration

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
from .views import query

from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^deploy/', include('deploy.urls', namespace='deploy')),
    # 生产环境下设置静态文件查找方式
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # 设置全文检索
    url(r'^search/', include('haystack.urls')),
    url(r'^query/', query, name='query'),  # 全文检索
]
