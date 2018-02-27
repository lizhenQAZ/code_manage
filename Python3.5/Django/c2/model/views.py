from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.db.models import F, Q, Sum, Count


# 一对多查询
def query_book(request):
    bookinfo = BookInfo.objects.get(pk=1)
    hero_list = bookinfo.heroinfo_set.all()
    for hero_info in hero_list:
        print(hero_info.hero_name)
    return HttpResponse('book')


def query_hero(request):
    heroinfo = HeroInfo.objects.get(pk=1)
    print(heroinfo.hero_book.book_title)
    return HttpResponse('hero')


# 一对一查询
def query_place(request):
    placeinfo = Place.objects.get(pk=1)
    print(placeinfo.restaurant.res_name)
    return HttpResponse('place')


def query_restaurant(request):
    resinfo = Restaurant.objects.get(pk=1)
    print(resinfo.res_place.place_name)
    return HttpResponse('restaurant')


# 非级联删除
def query_dormitory(request):
    dorminfo = Dormitory.objects.get(pk=1)
    dorminfo.delete()
    return HttpResponse('dormitory')


# 自定义管理器类
def query_manager(request):
    for index, item in enumerate(BookDesc.objects.all()):
        print("未删除的图书编号: ", index, " 未修改的图书名: ", item.book_title)
    # 修改图书标题
    book_desc = BookDesc.objects.with_new_name()
    for index, item in enumerate(book_desc):
        print("图书编号: ", index, " 修改后的图书名: ", item.book_title)
    return HttpResponse("这是自定义管理器类")


# 自定义查询集
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
    return HttpResponse("这是自定义查询集")


# 自关联查询
def query_join(request):
    first_area = AreaInfo.objects.filter(area_parent__area_name=None)
    print("一级地区名: ", first_area)
    second_area = AreaInfo.objects.filter(area_parent__area_name='北京')
    print("二级地区名: ", second_area)
    return HttpResponse("这是自关联查询")


# 结果集排序
def order(request):
    hero_list = HeroInfo.objects.all()
    print("类中定义英雄信息按id排列: ", hero_list)
    hero_list = HeroInfo.objects.order_by('id')
    print("英雄信息按id升序排列: ", hero_list)
    hero_list = HeroInfo.objects.order_by('-id')
    print("英雄信息按id降序排列: ", hero_list)
    return HttpResponse("结果集排序")


# 图书管理
def query_bookmanage(request):
    books = BookInfo.objects.filter(book_delete=False)
    return render(request, 'model/bookmanage.html', locals())


# 删除图书
def logicaldelete(request, param):
    print(param, type(param))
    book = BookInfo.objects.get(pk=param)
    book.book_delete = True
    book.save()
    return redirect("/model/bookmanage/")
