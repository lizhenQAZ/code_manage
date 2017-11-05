# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_comment, name='post'),
]
