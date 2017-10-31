from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'title', 'excerpt', 'author', 'category',
                    'created_time', 'modified_time']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
