from django.contrib import admin


from .models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_title', 'book_comment', 'book_read', 'book_delete', 'create_time', 'update_time']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hero_name', 'hero_sex', 'hero_desc', 'hero_delete', 'create_time', 'update_time']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
