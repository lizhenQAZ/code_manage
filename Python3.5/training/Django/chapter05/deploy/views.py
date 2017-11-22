from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


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


from .models import City


# 城市信息查询
def city(request):
    cities = City.objects.filter(area_parent=None)
    return render(request, "deploy/city.html", locals())


from django.http import JsonResponse


# 城市信息处理
def city_handle(request):
    # 获取返回的区号
    code = request.GET.get('code')
    # print("code: ", code)
    cities = City.objects.filter(area_parent=code)
    # print("cities: ", cities)
    result = list()
    for info in cities:
        temp = dict()
        temp['code'] = info.area_code
        temp['name'] = info.area_name
        # print(temp)
        result.append(temp)
    return JsonResponse({'ret': result})


# 自定义中间件处理流程
def middleware_process(request):
    print("这是视图函数!")
    return HttpResponse()


# 自定义中间件错误处理
def middleware_error(request):
    print("这是中间件错误处理视图函数!")
    1 + 's'
    return HttpResponse()


from .models import News


# 富文本编辑器编辑
def tinymce_edit(request):
    return render(request, 'deploy/news_edit.html', locals())


# 富文本编辑器保存数据
def tinymce_save(request):
    news = News()
    news.news_title = request.POST.get('title', '')
    news.news_content = request.POST.get('content', '')
    news.save()
    return redirect(reverse('deploy:tinymce_show'))


# 富文本编辑器显示
def tinymce_show(request):
    data = News.objects.all()
    return render(request, 'deploy/news_show.html', locals())


from django.core.mail import send_mail


# 发送邮件
def sendmail(request):
    """
        # subject 主题
        # message 邮件文本内容
        # from_email 发送者
        # recipient_list 收件人列表
        # auth_user 邮箱服务器认证用户
        # auth_password 认证密码
        # html_message html邮件内容
        def send_mail(subject, message, from_email, recipient_list,
                  fail_silently=False, auth_user=None, auth_password=None,
                  connection=None, html_message=None):
        """

    content = '<a href="http://www.baidu.com">请点击激活邮件!</a><em>斜体</em>'

    send_mail(subject='注册激活邮件',
              message='',
              from_email='lz15251847740@163.com',
              recipient_list=['516960831@qq.com', ],
              html_message=content, )

    return render(request, 'deploy/sendmail.html')


from . import tasks


# 设置celery
def celery(request):
    tasks.sayhello.delay()
    return HttpResponse('任务结束')


# 设置uwsgi+nginx
def uwsgi(request):
    return render(request, "deploy/uwsgi.html", locals())
