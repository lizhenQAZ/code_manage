# coding: utf-8
from django.core.urlresolvers import reverse
from utils.wrappers import set_cookie


class RecordUrlMiddleware:
    def process_response(self, request, response):
        exclude_urls = [
            reverse("user:register"),
            reverse("user:register_handle"),
            reverse("user:register_check_username"),
            reverse("user:login"),
            reverse("user:logout"),
            reverse("user:center"),
        ]
        if request.path not in exclude_urls and response.status_code == 200:
            set_cookie(response, 'pre_url', request.get_full_path())
        return response
