# 模板渲染
from django.shortcuts import render
# 视图响应
from django.shortcuts import HttpResponse
# 视图重定向
from django.shortcuts import redirect
# 视图反向解析
from django.core.urlresolvers import reverse
# 查询集
from django.db.models import F, Q, Sum, Count
# 模型类
from .models import *


# 模板首页
def index(request):

    return render(request, "model/index.html", locals())


# 一对多查询
# 单字段
def query_book(request):
    bookinfo = BookInfo.objects.get(pk=1)
    print(bookinfo)
    heros = bookinfo.heroinfo_set.all()
    print(heros)
    return render(request, 'model/book.html', locals())


# 多字段
def query_hero(request):
    heroinfo = HeroInfo.objects.get(pk=1)
    print(heroinfo)
    book = heroinfo.hero_book
    print(book)
    return render(request, 'model/hero.html', locals())


# 一对一查询
def query_place(request):
    placeinfo = Place.objects.get(pk=1)
    print(placeinfo)
    restinfo = placeinfo.restaurant
    print(restinfo)
    return render(request, 'model/place.html', locals())


def query_restaurant(request):
    restinfo = Restaurant.objects.get(pk=1)
    print(restinfo)
    placeinfo = restinfo.rest_place
    print(placeinfo)
    return render(request, 'model/restaurant.html', locals())


# 非级联删除
def query_dormitory(request):
    dorminfo = Dormitory.objects.get(pk=1)
    print(dorminfo)
    dorminfo.delete()
    memberinfo = Member.objects.all()
    print(dorminfo)
    return render(request, 'model/dormitory.html', locals())


# 自定义管理器类
def query_manager(request):
    bookinfo = BookDesc.objects.all()
    for index, item in enumerate(bookinfo):
        print("未删除的图书编号: ", index, " 未修改的图书名: ", item.book_title)
    # 修改图书标题
    bookinfomodified = BookDesc.objects.with_new_name()
    for index, item in enumerate(bookinfomodified):
        print("图书编号: ", index, " 修改后的图书名: ", item.book_title)
    return render(request, 'model/manager.html', locals())


# 查询集
def query_set(request):
    print('='*20, ' all获得所有对象 ', '='*20)
    all_books = BookDesc.objects.all()
    print("图书中的所有对象:", all_books, " 对象长度: ", len(all_books))
    spec_books = BookInfo.objects.all()[:1]
    print("图书中的指定对象:", spec_books, " 对象长度: ", len(spec_books))
    print('='*20, ' 过滤器获得对象 ', '='*20)
    book_exact = BookDesc.objects.filter(id__exact=1)
    print("exact过滤器: ", book_exact)
    book_contains = BookDesc.objects.filter(book_title__contains='龙')
    print("contains过滤器: ", book_contains)
    book_startswith = BookDesc.objects.filter(book_title__startswith='雪')
    print("startswith过滤器: ", book_startswith)
    book_endswith = BookDesc.objects.filter(book_title__endswith='狐')
    print("endswith过滤器: ", book_endswith)
    book_isnull = BookDesc.objects.filter(book_title__isnull=True)
    print("isnull过滤器: ", book_isnull)
    book_in = BookDesc.objects.filter(id__in=[1, 2])
    print("in过滤器: ", book_in)
    book_gt = BookDesc.objects.filter(id__gt=1)
    print("gt过滤器: ", book_gt)
    book_gte = BookDesc.objects.filter(id__gte=1)
    print("gte过滤器: ", book_gte)
    book_lt = BookDesc.objects.filter(id__lt=1)
    print("lt过滤器: ", book_lt)
    book_lte = BookDesc.objects.filter(id__lte=1)
    print("lte过滤器: ", book_lte)
    book_iexact = BookDesc.objects.filter(id__iexact=1)
    print("iexact过滤器: ", book_iexact)
    book_icontains = BookDesc.objects.filter(book_title__icontains='龙')
    print("icontains过滤器: ", book_icontains)
    book_istartswith = BookDesc.objects.filter(book_title__istartswith='雪')
    print("istartswith过滤器: ", book_istartswith)
    book_iendswith = BookDesc.objects.filter(book_title__iendswith='狐')
    print("iendswith过滤器: ", book_iendswith)
    print('='*20, ' get获得单一对象 ', '='*20)
    book_get = BookDesc.objects.get(book_title='天龙八部')
    print("get获得对象: ", book_get)
    print('='*20, ' F对象和Q对象 ', '='*20)
    book_fobj = BookDesc.objects.filter(book_read__gte=F('book_comment')*1)
    print('F对象: ', book_fobj)
    book_qobj = BookDesc.objects.filter(Q(book_read=20) | Q(book_comment=40))
    print('Q对象: ', book_qobj)
    print('='*20, ' 聚合函数 ', '='*20)
    book_sum = BookDesc.objects.aggregate(Sum('book_comment'))
    print('Sum聚合函数: ', book_sum)
    book_count = BookDesc.objects.aggregate(Count('id'))
    print('Count聚合函数: ', book_count)
    book_count_new = BookDesc.objects.count()
    print('count聚合函数: ', book_count_new)
    print('='*20, ' 关联查询 ', '='*20)
    hero_name = HeroInfo.objects.filter(hero_book__book_title="天龙八部")
    print('外键查询英雄名: ', hero_name)
    book_title = BookInfo.objects.filter(heroinfo__hero_name="乔峰")
    print('类查询书名: ', book_title)
    return render(request, 'model/queryset.html', locals())


# 自关联查询
def query_join(request):
    first_areas = AreaInfo.objects.filter(area_parent__area_name=None)
    print("一级地区名: ", first_areas)
    second_areas = AreaInfo.objects.filter(area_parent__area_name='北京')
    print("二级地区名: ", second_areas)
    return render(request, 'model/join.html', locals())


# 结果集排序
def order(request):
    heros_id = HeroInfo.objects.all()
    print("类中定义英雄信息按id排列: ", heros_id)
    heros_name = HeroInfo.objects.order_by('hero_name')
    print("英雄信息按名称升序排列: ", heros_name)
    heros_minusname = HeroInfo.objects.order_by('-hero_name')
    print("英雄信息按名称降序排列: ", heros_minusname)
    return render(request, 'model/order.html', locals())


# 图书管理
# 显示图书
def query_bookmanage(request):
    books = BookInfo.objects.filter(is_deleted=False)
    return render(request, 'model/bookmanage.html', locals())


# 删除图书
def logicaldelete(request, param):
    # print(param, type(param))
    book = BookInfo.objects.get(pk=param)
    book.is_deleted = True
    book.save()
    return redirect(reverse('model:bookmanage'))
