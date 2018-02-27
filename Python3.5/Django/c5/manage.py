#!/usr/bin/env python
"""
功能点：
1.静态文件处理
2.文件上传
3.分页器
4.自关联查询
5.中间件处理
6.富文本编辑器
7.发送邮件
8.异步通讯
9.uwsgi服务器
10.自定义中间件处理、视图函数处理流程
11.全文索引
"""


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c5.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
