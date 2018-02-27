from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse


# url不定长参数反向解析
def urlreverse(request, param):
    redirect_url = reverse('view:urlreverse', args=(1,))
    print("重定向地址: ", redirect_url)
    return HttpResponse("这是url不定长参数反向解析")


# url关键字参数反向解析
def urlreversekey(request, num):
    print(num)
    redirect_url = reverse('view:urlreversekey', kwargs={'num': num})
    print("重定向地址: ", redirect_url)
    return HttpResponse("这是url关键字参数反向解析")


# 自定义404错误处理
def handle404(request):
    return HttpResponse("发生了404错误!")


# 自定义500错误处理
def handle500(request):
    return HttpResponse("发生了500错误!")


# 自定义403错误处理
def handle403(request):
    return HttpResponse("发生了403错误!")


# 产生get请求
def urlget(request):
    html = '<a href="/view/urlgetsolve/?a=5&b=10">产生get请求</a>'
    return HttpResponse(html)


# 处理get请求
def urlgetsolve(request):
    print("请求路径: ", request.path)
    print("请求方法: ", request.method)
    print("请求get所有参数:", request.GET)
    print("请求post所有参数:", request.POST)
    print("请求files参数:", request.FILES)
    print("请求cookies参数:", request.COOKIES)
    print("请求session参数:", request.session)
    return HttpResponse('处理get请求')


# 产生post请求
def urlpost(request):
    return render(request, 'view/post.html')


# 处理post请求
def urlpostsolve(request):
    print("请求路径: ", request.path)
    print("请求方法: ", request.method)
    print("请求get所有参数:", request.GET)
    print("请求post所有参数:", request.POST)
    print("请求files参数:", request.FILES)
    print("请求cookies参数:", request.COOKIES)
    print("请求session参数:", request.session)
    return HttpResponse('处理post请求')


# 自定义HttpResponse响应
def urlresponse(request):
    response = HttpResponse(content='<h1>这是view视图</h1>')
    response.write('<h2>这是HttpResponse响应</h2>')
    response.status_code = 200
    response.reason_phrase = 'ok'
    print("HttpResponse响应的长度: ", response.tell())
    print("HttpResponse响应的内容: ", response.getvalue())
    return response


# 自定义redirect响应
def urlredirect(request):
    redirect_url = HttpResponseRedirect('/')
    return redirect_url


# 自定义redirect响应方式二
def urlredirectshort(request):
    redirect_url = redirect('/')
    return redirect_url


# 自定义ajax响应
def ajax(request):
    # 获取POST参数
    a = request.GET.get('a')
    b = request.GET.get('b')
    if a and b:
        a = int(a)
        b = int(b)
        content = "运算结果为: %d + %d = %d" % (a, b, a+b)
        return JsonResponse({'result': content})
    else:
        return render(request, 'view/ajax.html')


# 设置cookie
def cookieset(request):
    response = HttpResponse("已经设置了cookie!")
    response.set_cookie('name', 'lizhen', max_age=30, path='/')
    return response


# 获取cookie
def cookieget(request):
    cookie = request.COOKIES.get('name')
    print("cookie的name值: ", cookie)
    return HttpResponse('获取cookie结束!')


# 删除cookie
def cookiedel(request):
    response = HttpResponse("正准备删除cookie")
    cookie = response.delete_cookie('name')
    print("删除cookie的name值: ", cookie)
    return response


# 设置session
def sessionset(request):
    request.session['name'] = 'lizhen'
    return HttpResponse("设置了session!")


# 获取session
def sessionget(request):
    session = request.session.get('name')
    print("session的name值: ", session)
    return HttpResponse('获取session结束!')


# 删除session
def sessiondel(request):
    print("删除指定的session")
    del request.session['name']
    print("删除所有session")
    request.session.flush()
    return HttpResponse("删除session结束")
