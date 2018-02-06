#-*-coding:utf-8-*-
from django.shortcuts import render


# 网站首页
def index(request):

    return render(request, "index.html", locals())
