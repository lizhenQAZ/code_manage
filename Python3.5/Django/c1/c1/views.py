from django.http import HttpResponse


# 定义首页的响应函数
def index(request):
    return HttpResponse("这是响应视图")
