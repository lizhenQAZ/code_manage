from django.conf.urls import url


# 引入视图模块
from .views import *

urlpatterns = [
    url(r'^template1/$', template1),  # 模板响应方式一
    url(r'^template2/$', template2),  # 模板响应方式二
    url(r'^case/$', case),
    url(r'^detail/(\d+)/$', detail),
]
