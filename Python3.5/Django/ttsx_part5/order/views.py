from django.shortcuts import render
from carts.models import *
from users.models import *
from utils.wrappers import *


# 订单
def place_order(request):
    # 获取所有商品id
    goods_id = post_list(request, 'goods_id')
    print(goods_id)
    # 获取所有商品
    carts = Carts.objects.filter(cart_user_id=get_session(request, 'uid'), cart_goods_id__in=goods_id)
    print(carts)
    # 记录商品总价
    carts.total = 0
    # 记录商品总量
    carts.amount = 0
    for cart in carts:
        # 记录商品单品总价
        cart.single = cart.cart_goods.goods_price * cart.cart_amount
        print(cart.single)
        carts.total += cart.single
        carts.amount += cart.cart_amount
    # 查找个人信息
    user = User.objects.user_by_username(get_session(request, 'user_name'))

    return render(request, 'order/place_order.html', locals())
