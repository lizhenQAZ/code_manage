from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'gender', 'hcontent']


class HeroInfoInline(admin.TabularInline):  # 可以将内嵌的方式改为表格
# class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)
