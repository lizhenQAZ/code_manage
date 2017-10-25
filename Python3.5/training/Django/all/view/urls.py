from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),  # view首页
    url(r'^error500/$', views.error500, name="error500"),  # 产生500错误
    url(r'^urlreverse/(.*)/$', views.urlreverse, name="urlreverse"),  # 视图中不定常参数反向解析
    url(r'^urlreversekey/(?P<num>.*)/$', views.urlreversekey, name="urlreversekey"),  # 视图中关键字参数反向解析
    url(r'^urlget/$', views.urlget, name="urlget"),  # 产生get请求
    url(r'^urlgetsolve/', views.urlgetsolve, name="urlgetsolve"),  # 处理get请求
    url(r'^urlpost/$', views.urlpost, name="urlpost"),  # 产生post请求
    url(r'^urlpostsolve/$', views.urlpostsolve, name="urlpostsolve"),  # 处理post请求
    url(r'^urlresponse/$', views.urlresponse, name="urlresponse"),  # 产生response响应
    url(r'^urlredirect/$', views.urlredirect, name="urlredirect"),  # 产生redirect响应
    url(r'^urlredirectshort/$', views.urlredirectshort, name="urlredirectshort"),  # 产生redirect响应方式二
    url(r'^ajax/$', views.ajax, name="ajax"),  # 产生ajax响应
    url(r'^cookieset/$', views.cookieset, name="cookieset"),  # 设置cookie
    url(r'^cookieget/$', views.cookieget, name="cookieget"),  # 获得cookie
    url(r'^cookiedel/$', views.cookiedel, name="cookiedel"),  # 删除cookie
    url(r'^sessionset/$', views.sessionset, name="sessionset"),  # 设置session
    url(r'^sessionget/$', views.sessionget, name="sessionget"),  # 获得session
    url(r'^sessiondel/$', views.sessiondel, name="sessiondel"),  # 删除session
]