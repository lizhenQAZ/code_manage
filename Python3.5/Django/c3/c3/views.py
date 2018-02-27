# coding=utf-8
from django.shortcuts import HttpResponse


# 定义网站首页
def index(request):
    # 产生500错误
    1 + 's'
    return HttpResponse("这是网站首页")
