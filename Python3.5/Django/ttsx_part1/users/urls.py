#-*-coding:utf-8-*-


from django.conf.urls import url


from .views import *

urlpatterns = [
    url(r'^register/$', register, name='register'),  # 用户注册
    url(r'^login/$', login, name='login'),  # 用户登录
    url(r'^user_center_info/$', user_center_info, name='user_center_info'),  # 用户中心信息
    url(r'^user_center_site/$', user_center_site, name='user_center_site'),  # 用户中心地址
    url(r'^user_center_order/$', user_center_order,  name='user_center_order'),  # 用户中心订单
    url(r'^register_handle/$', register_handle, name='register_handle'),  # 用户注册处理
]
