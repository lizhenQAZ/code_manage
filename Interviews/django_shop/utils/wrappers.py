# coding: utf-8
from django.contrib import messages
from hashlib import sha256


def post(request, key):
    return request.POST.get(key, '').strip()


def add_message(request, key, message):
    message = key + ':' + message
    messages.add_message(request, messages.INFO, message)


def get_message(request):
    message = messages.get_messages(request)
    info = {}
    for mess in message:
        temp = str(mess).split(":")
        info[temp[0]] = temp[1]
    return info


def encrypt_password(password, salt=""):
    s256 = sha256()
    password = "!@##@@@" + password + "!^^&^&^&" + salt
    s256.update(password.encode())
    return s256.hexdigest()


def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


def get_cookie(request, key):
    return request.COOKIES.get(key, '')


def del_cookie(response, key):
    response.del_cookie(key)


def set_session(request, key, value):
    request.session[key] = value


def get_session(request, key):
    return request.session.get(key, '').strip()


def del_session(request):
    request.session.flush()
