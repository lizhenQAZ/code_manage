#-*-coding:utf-8-*-
import hashlib
from django.contrib import messages

# post
def post(request, key):
    return request.POST.get(key, '').strip()


# get
def get(request, key):
    return request.GET.get(key, '').strip()


# 密码加密
def password_encryption(password, salt=''):
    sha = hashlib.sha256()
    new_password = 'nbcnhadscvgvacgv' + password + 'cbmhacvgvagZcv' + salt
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()


# add_message
def add_message(request, key, value):
    message = key + ':' + value
    messages.add_message(request, messages.INFO, message)


# def get_messages
def get_messages(request):
    message = messages.get_messages(request)
    info = dict()
    for item in message:
        tmp = str(item).split(':')
        info[tmp[0]] = tmp[1]
    return info
