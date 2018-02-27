# coding=utf-8
from django.shortcuts import HttpResponse


# 网站首页
def index(request):
    return HttpResponse("这是网站首页!")
