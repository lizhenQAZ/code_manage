from django.shortcuts import render


# 商品首页
def index(request):
    return render(request, 'goods/index.html', locals())


# 商品列表
def goods_list(request):
    return render(request, 'goods/list.html', locals())


# 商品详情
def detail(request):
    return render(request, 'goods/detail.html', locals())
