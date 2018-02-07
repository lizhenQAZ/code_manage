# coding: utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^register_check_username/$', views.register_check_username, name='register_check_username'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^center/$', views.center, name='center'),
    url(r'^handle/$', views.handle, name='handle'),
]
