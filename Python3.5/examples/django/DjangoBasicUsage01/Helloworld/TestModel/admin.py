from django.contrib import admin


# Register your models here.
from .models import Test, Contact, Tag


# 全部显示
# admin.site.register([Test, Contact, Tag])


# 部分显示
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])


# 隐藏显示
# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # css
#             'fields': ('age',),
#         }]
#     )
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])


# 内联显示
# class TagInline(admin.TabularInline):
#     model = Tag
#
#
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [TagInline]
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # css
#             'fields': ('age',),
#         }]
#     )
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test])


# 列表显示
# class TagInline(admin.TabularInline):
#     model = Tag
#
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'email')
#     inlines = [TagInline]
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # css
#             'fields': ('age',),
#         }]
#     )
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test])


# 搜索栏显示
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # css
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
