from django.shortcuts import render


# 显示静态文件
def staticfile(request):
    return render(request, 'deploy/staticfile.html')


# 文件上传
def fileupload(request):
    return render(request, "deploy/upload.html")


from .models import MyFile
from django.conf import settings
from django.shortcuts import HttpResponse


# 文件上传处理
def fileuploadhandle(request):
    if request.method == 'POST':
        # 获得文件数据对象
        myfile = request.FILES.get('myfile', None)
        if myfile:
            print("上传文件名称:", myfile.name)
            # 保存文件路径到数据库
            f = MyFile(file_name=myfile.name)
            f.save()
            # 保存文件到服务器
            fname = settings.MEDIA_ROOT + '/deploy/' + myfile.name
            print("fname:", fname)
            with open(fname, 'wb') as f:
                # 一次写入64K内容
                for data in myfile.chunks():
                    f.write(data)
    return HttpResponse('成功!')


from .models import AreaInfo
from django.core.paginator import *


# 分页器处理
def paginator(request):
    # 查询所有数据
    area_all_data = AreaInfo.objects.all()
    # 对数据分页, 每页10条数据
    paginator = Paginator(area_all_data, 10, 0)
    # 获得当前页码
    page_now = request.GET.get('page_now', None)
    try:
        page_data_list = paginator.page(page_now)
    except PageNotAnInteger:
        page_now = 1
        page_data_list = paginator.page(page_now)
    except EmptyPage:
        if int(page_now) <= 0:
            page_now = 1
        else:
            page_now = paginator.num_pages
        page_data_list = paginator.page(page_now)

    context = {"page_now": page_data_list,
               "page_index": paginator.page_range,
               'cur_page': page_now, }

    return render(request, 'deploy/paginator.html', context)
