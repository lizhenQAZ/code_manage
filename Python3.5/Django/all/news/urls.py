from django.conf.urls import url


# 引入视图模块
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # news首页
    url(r'^template_full/$', views.template_full, name='template_full'),  # 模板完整处理
    url(r'^template_brief/$', views.template_brief, name='template_brief'),  # 模板简单处理
    url(r'^news_list/$', views.news_list, name='news_list'),  # 新闻列表
    url(r'^news_detail/(\d+)/$', views.news_detail, name='news_detail'),  # 新闻详情
]
