from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^staticfile/$', views.staticfile, name='staticfile'),  # 静态文件显示
    url(r'^fileupload/$', views.fileupload, name='fileupload'),  # 文件上传显示
    url(r'^fileuploadhandle/$', views.fileuploadhandle, name='fileuploadhandle'),  # 文件上传处理
    url(r'^paginator/$', views.paginator, name='paginator'),  # 数据分页处理
    url(r'^city/$', views.city, name='city'),  # 城市信息查询
    url(r'^city_handle/$', views.city_handle, name='city_handle'),  # 城市信息处理查询
    url(r'^middleware_process/$', views.middleware_process, name='middleware_process'),  # 自定义中间件处理流程
    url(r'^middleware_error/$', views.middleware_error, name='middleware_error'),  # 自定义中间件错误视图
    url(r'^tinymce_edit/$', views.tinymce_edit, name='tinymce_edit'),  # 富文本编辑器视图
    url(r'^tinymce_save/$', views.tinymce_save, name='tinymce_save'),  # 富文本编辑器保存
    url(r'^tinymce_show/$', views.tinymce_show, name='tinymce_show'),  # 富文本编辑器显示
    url(r'^sendmail/$', views.sendmail, name='sendmail'),  # 发送邮件
    url(r'^celery/$', views.celery, name='celery'),  # celery发送邮件
    url(r'^uwsgi/$', views.uwsgi, name='uwsgi'),  # uwsgi服务器
]
