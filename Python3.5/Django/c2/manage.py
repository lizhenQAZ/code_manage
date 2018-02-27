#!/usr/bin/env python
"""
功能点：
1.一对多、一对一查询
2.非级联删除、逻辑删除
3.自定义管理器
4.自定义查询集
5.自关联查询
6.结果集排序
7.自定义模型表名、自定义抽象模型、自定义模型所有类型
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c2.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
