#-*-coding:utf-8-*-


from django.core.urlresolvers import reverse
from utils.wrappers import *


# 记录url中间件
class RecordUrlMiddleware(object):

    def process_request(self, request):
        exclude_url = [
            reverse('users:register'),
            reverse('users:login'),
            reverse('users:register_handle'),
            reverse('users:register_check_username'),
            reverse('users:login_handle'),
            reverse('users:logout'),
            reverse('users:user_center_info'),
            reverse('users:user_center_site'),
            reverse('users:user_center_order'),
        ]
        if request.path not in exclude_url:
            set_session(request, 'pre_url', request.get_full_path())
