#!/usr/bin/env python
"""
功能点：
1.自定义错误视图：
指定handler404视图函数返回响应
未指定指定handler404视图函数，从templates文件夹下寻找404.html文件返回响应或者返回默认响应
2.参数反向解析、request参数、response参数、JsonResponse
3.get请求与post请求、重定向
4.cookie与session
response.set_cookie(key, value)
request.COOKIES.get(key, '')
response.delete_cookie(key)
request.session[key] = value
request.session.get(key, '')
del request.session[key]或者request.session.flush()
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c3.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
