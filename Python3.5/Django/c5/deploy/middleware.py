#-*-coding:utf-8-*-
from django.shortcuts import HttpResponse


# ip黑名单
class IpsForbidden(object):
    def process_request(self, request):
        # 禁止ip列表
        forbidden_ip = ['192.168.0.1', '192.168.254.132', '192.168.122.1', ]
        # 获得用户ip
        remote_ip = request.META.get('REMOTE_ADDR')
        print('remote_ip', remote_ip)
        # 判断用户ip
        if remote_ip in forbidden_ip:
            return HttpResponse('<h1>您的ip是%s，remote_ip, Forbidden!</h1>' % remote_ip)


# 自定义中间件处理流程
class MyCustomProcess(object):
    def __init__(self):
        print("MyCustomProcess __init__!")

    def process_request(self, request):
        print("MyCustomProcess process_request!")

    def process_view(self, request, view_func, *args, **kwargs):
        print("MyCustomProcess process_view!")

    def process_response(self, request, response):
        print("MyCustomProcess process_response!")
        return HttpResponse()


# 自定义中间件错误视图处理
class MyCustomError(object):
    def process_exception(self, request, exception):
        print('这是错误日志:', exception)
        return HttpResponse("服务器繁忙，请稍后再试！")
