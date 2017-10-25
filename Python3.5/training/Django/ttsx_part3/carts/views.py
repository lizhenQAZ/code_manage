from django.shortcuts import render


# 购物车
def cart(request):
    return render(request, 'carts/cart.html', locals())
