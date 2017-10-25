from django.shortcuts import render


# 订单
def place_order(request):
    return render(request, 'order/place_order.html', locals())
