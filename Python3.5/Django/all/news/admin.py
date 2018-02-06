from django.contrib import admin


# 导入模型类模块
from .models import *


# 管理模型类
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cag_name']


class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'news_title', 'news_content', 'news_category_id']


# 注册模型类
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(NewsInfo, NewsInfoAdmin)
