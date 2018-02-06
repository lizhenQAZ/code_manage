from django.shortcuts import render
# 自定义模型类
from .models import *
# 包装类
from utils.wrappers import *


# 商品首页
def index(request):
    # 获取广告分类
    ads = Advertisement.objects.all()
    adv1 = ads[:4]
    adv2 = ads[4:]
    # 获取商品分类
    cags = Category.objects.all()
    for cag in cags:
        # 获取最热的三个商品
        hot = GoodsInfo.objects.get_hot_by_cag(cag)
        # 获取最新的的四个商品
        new = GoodsInfo.objects.get_new_by_cag(cag)
        cag.hot = hot
        cag.new = new

    return render(request, 'goods/index.html', locals())


# 商品列表
def goods_list(request):

    return render(request, 'goods/list.html', locals())


# 商品详情
def detail(request):
    # 获取查询的商品
    goods = GoodsInfo.objects.get(pk=int(get(request, 'id')))
    goods_hot_all = GoodsInfo.objects.get_hot_by_all()
    return render(request, 'goods/detail.html', locals())
