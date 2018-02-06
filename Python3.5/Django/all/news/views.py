# 模板加载
from django.shortcuts import render
from django.template import loader
# 视图响应
from django.http import HttpResponse
# 模型类
from .models import *


# 新闻首页
def index(request):

    return render(request, 'news/index.html', locals())


# 模板完整处理
def template_full(request):
    # 1.读入模板文件
    template = loader.get_template("news/template.html")
    # 2.设置模板传递参数
    context = {"title": "军事新闻", 'content': "大战一触即发", 'style': "模板完整处理"}
    # 3.渲染模板
    new_template = template.render(context)

    return HttpResponse(new_template)


# 模板简单处理
def template_brief(request):
    style = "模板简单处理"
    title = "军事新闻"
    content = "大战一触即发"

    return render(request, 'news/template.html', locals())


# 新闻列表
def news_list(request):
    # 读取新闻分类
    cags = NewsCategory.objects.all()
    print('news_category: ', cags)

    return render(request, 'news/news_list.html', locals())


# 新闻详情
def news_detail(request, cag_id):
    # 读取指定新闻
    cag = NewsCategory.objects.get(pk=cag_id)
    # 读取新闻详情
    details = cag.newsinfo_set.all()

    return render(request, 'news/news_detail.html', locals())
