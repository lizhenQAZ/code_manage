#!/usr/bin/env python
"""
功能点：
1.for循环控制、if判断
2.逻辑操作符、集合操作符、算术操作符
3.注释、模板函数、模板继承、包含与替换、转义
4.生成验证码
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c4.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
