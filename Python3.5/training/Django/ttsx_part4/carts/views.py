from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from utils.wrappers import *


# 购物车
def cart(request):

    return render(request, 'carts/cart.html', locals())


# 商品加入购物车
def add_carts(request):
    user_id = get_session(request, 'uid')
    user_name = get_session(request, 'user_name')
    print(user_id, user_name)
    # 1.判断用户是否登录
    if not (user_id and user_name):

        return JsonResponse({'total': 0})
    # 2.获取商品信息
    goods_id = get(request, 'goods_id')
    goods_num = get(request, 'goods_num')
    print('goods_id: ', goods_id, 'goods_num: ', goods_num)
    # 3.信息入库
    try:
        # 3.1 如果商品已经存在，则更新商品数量和修改时间
        record = Carts.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        record.cart_amount = record.cart_amount + int(goods_num)
        record.save()
    except Carts.DoesNotExist:
        # 3.2 如果商品不存在，则更新用户信息、商品数量和商品信息
        record = Carts()
        record.cart_goods_id = goods_id
        record.cart_user_id = user_id
        record.cart_amount = goods_num
        record.save()
    # 4.返回购物车总数
    total = Carts.objects.filter(cart_user_id=user_id).aggregate(models.Sum("cart_amount"))
    print(total['cart_amount__sum'])

    return JsonResponse({'total': total['cart_amount__sum']})
