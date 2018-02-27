# coding=utf-8
from django.shortcuts import render


# 设置全文索引
def query(request):
    return render(request,'deploy/query.html')
