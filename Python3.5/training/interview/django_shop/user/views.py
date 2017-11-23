from django.shortcuts import render
from .functions import check_params, check_login_params, save_cookie, keep_online_status, get_redirect_url, check_user
from utils.wrappers import get_message, post, get_cookie, del_session
from django.shortcuts import redirect
from .models import User
from django.http import JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
import time
import json


def register(request):
    messages = get_message(request)
    return render(request, 'user/register.html', locals())


def register_handle(request):
    # 检查传入参数
    # 正确，注册成功，数据存入数据库, 返回登录界面
    if check_params(request):
        User.objects.save_user(request)
        return redirect(reverse('user:login'))
    # 错误，注册失败，返回错误信息，重新注册
    else:
        return redirect(reverse('user:register'))


def register_check_username(request):
    if User.objects.user_by_username(post(request, 'user_name')):
        ret = 0
    else:
        ret = 1
    return JsonResponse(locals())


def login(request):
    if request.method == 'POST':
        # 正确，保存session和cookie,返回商品页面
        if check_login_params(request):
            redirect_url = get_redirect_url(request)
            response = redirect(redirect_url)
            save_cookie(request, response)
            keep_online_status(request)
            return response
        # 错误，返回登录页面，显示商品信息
        messages = get_message(request)
    return render(request, 'user/login.html', locals())


def logout(request):
    # 删除session, 返回访问前的页面
    redirect_url = get_redirect_url(request)
    response = redirect(redirect_url)
    del_session(request)
    return response


def index(request):
    return render(request, "goods/index.html", locals())


@check_user
def center(request):
    return render(request,  "user/user_center_info.html", locals())


def handle(request):
    result = request.GET.get("name", "")
    if result:
        time.sleep(2)
        return JsonResponse({'ret': 1}, content_type="text/javascript")
    return JsonResponse({'ret': 0}, content_type="text/javascript")
