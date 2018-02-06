from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *


# 定义首页的响应函数
def index(request):
    return HttpResponse("这是响应视图")


# 定义模板函数方式一
def template1(request):
    template = loader.get_template("news/template.html")
    context = {"title": "军事新闻", 'content': "大战一触即发"}
    new_template = template.render(context)
    return HttpResponse(new_template)


# 定义模板函数方式二
def template2(request):
    title = "军事新闻"
    content = "大战一触即发"
    return render(request, 'news/template.html', locals())


# 定义新闻首页
def case(request):
    # 读取商品分类信息
    category = NewsCategory.objects.all()
    print(category)
    return render(request, 'news/case.html', locals())


# 定义新闻内容
def detail(request, cag_id):
    # 读取商品分类信息
    cag = NewsCategory.objects.get(pk=cag_id)
    news_list = cag.newsinfo_set.all()
    return render(request, 'news/detail.html', locals())
