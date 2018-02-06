# coding: utf-8
from utils.wrappers import post, encrypt_password, set_cookie, set_session
import re
from .models import User
from utils.wrappers import add_message, get_cookie, get_session
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def check_params(request):
    user = post(request, 'user_name')
    pwd = post(request, 'pwd')
    cpwd = post(request, 'cpwd')
    email = post(request, 'email')
    flag = True
    # 用户名的长度在5~20之间
    if not (5 <= len(user) <= 20):
        flag = False
        add_message(request, 'user_name', "用户名的长度不在5~20之间")
    # 密码的长度在8~20之间
    if not (8 <= len(pwd) <= 20):
        flag = False
        add_message(request, 'pwd', "密码的长度不在8~20之间")
    regex = "^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$"
    # 邮箱是否符合要求
    if not re.match(regex, email):
        flag = False
        add_message(request, 'email', "邮箱不符合格式要求")
    # 密码是否一致
    if pwd != cpwd:
        flag = False
        add_message(request, 'cpwd', "两次密码不一致")
    # 用户名是否已经存在
    if (5 <= len(user) <= 20) and User.objects.user_by_username(user):
        flag = False
        add_message(request, 'user_name', "用户名已经存在")
    return flag


def check_login_params(request):
    user = post(request, 'username')
    pwd = post(request, 'pwd')
    flag = True
    if not (5 <= len(user) <= 20):
        flag = False
        add_message(request, 'username', "用户名的长度不在5~20之间")
    if not (8 <= len(pwd) <= 20):
        flag = False
        add_message(request, 'userpwd', "密码的长度不在8~20之间")
    username = User.objects.user_by_username(user)
    if not username:
        flag = False
        add_message(request, 'username', "用户名不存在")
    else:
        if username.pwd != encrypt_password(pwd):
            flag = False
            add_message(request, 'userpwd', "用户密码不正确")
    return flag


def save_cookie(request, response):
    reme = post(request, 'reme')
    if reme:
        set_cookie(response, 'user', post(request, 'username'))


def keep_online_status(request):
    set_session(request, 'user', post(request, 'username'))


def get_redirect_url(request):
    url = get_cookie(request, 'pre_url')
    if not url:
        url = reverse("user:center")
    return url


def check_user(func):
    def test(request, *args, **kwargs):
        if not get_session(request, 'user'):
            return redirect(reverse("user:login"))
        else:
            return func(request, *args, **kwargs)
    return test
