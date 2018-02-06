#-*-coding:utf-8-*-


from utils.wrappers import *
import re
from .models import *


# 检查注册参数
def check_register_param(request):
    username = post(request, 'user_name')
    userpwd = post(request, 'user_pwd')
    usercpwd = post(request, 'user_cpwd')
    usermail = post(request, 'user_mail')

    flag = True
    # 判断用户名长度
    if not (5 <= len(username) <= 20):
        flag = False
        add_message(request, 'user_name', '用户名不在5~20之间!')

    # 判断用户密码长度
    if not (8 <= len(userpwd) <= 20):
        flag = False
        add_message(request, 'user_pwd', '用户密码不在8~20之间!')

    # 判断邮箱是否符合格式
    regex = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(regex, usermail):
        flag = False
        add_message(request, 'user_mail', '用户密码不符合邮箱格式!')

    # 判断两次密码是否一致
    if userpwd != usercpwd:
        flag = False
        add_message(request, 'user_pwd', '两次密码不一致!')

    # 判断用户名是否存在
    if User.objects.user_by_username('user_name'):
        flag = False
        add_message(request, 'user_name', '用户名已经存在!')

    return flag
