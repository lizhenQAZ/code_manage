from django.shortcuts import render
from django.template import loader


# 创建视图
from django.http import HttpResponse


# 直接响应
def index(request):
    return HttpResponse("hello guests!")


# 拼接html
def hello(request):
    # 获取模板文件
    tpl = loader.get_template("hello.html")
    # 设置上下文
    ctx = {'title': '军事新闻', 'content': '争端'}
    # 渲染模板
    render_tpl = tpl.render(ctx)
    # 返回请求
    return HttpResponse(render_tpl)
