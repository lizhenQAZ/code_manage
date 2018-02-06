from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .functions import *
from utils.wrappers import *


# 注册
def register(request):
    infos = get_messages(request)
    print(infos)
    return render(request, 'users/register.html', locals())


# 登陆
def login(request):
    return render(request, 'users/login.html', locals())


# 用户中心信息
def user_center_info(request):
    return render(request, 'users/user_center_info.html', locals())


# 用户中心地址
def user_center_site(request):
    return render(request, 'users/user_center_site.html', locals())


# 用户中心订单
def user_center_order(request):
    return render(request, 'users/user_center_order.html', locals())


# 注册处理
def register_handle(request):
    # 检查参数
    # 验证通过
    if check_register_param(request):
        # 1.数据入库
        User.objects.user_register_save(request)
        # 2.返回登陆界面
        return redirect(reverse("users:login"))
    # 验证失败
    else:
        # 返回注册页面
        return redirect(reverse("users:register"))

