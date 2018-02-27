# coding=utf-8
from django.shortcuts import HttpResponse


# 定义首页
def index(request):
    return HttpResponse("<h1>这是首页内容</h1>")
