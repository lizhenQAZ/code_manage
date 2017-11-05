from django.contrib import admin
from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_time', 'update_time']


class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_time', 'update_time']


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'body', 'excerpt', 'cag', 'author', 'created_time', 'update_time']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
