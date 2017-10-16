from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^staticfile/$', views.staticfile, name='staticfile'),  # 静态文件显示
    url(r'^fileupload/$', views.fileupload, name='fileupload'),  # 文件上传显示
    url(r'^fileuploadhandle/$', views.fileuploadhandle, name='fileuploadhandle'),  # 文件上传处理
    url(r'^paginator/$', views.paginator, name='paginator'),  # 数据分页处理
]
