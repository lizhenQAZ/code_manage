from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'link', 'content', 'post', 'created_time', 'update_time', 'is_deleted']

admin.site.register(Comment, CommentAdmin)
