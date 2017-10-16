from django.contrib import admin

from .models import *


# 文件管理类
class MyFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_name']

# 注册模型类
admin.site.register(MyFile, MyFileAdmin)


# 内嵌式模型
# 块方式
# class PersonInline(admin.StackedInline):
#     model = Person  # 内嵌模型
# extra = 1  # 新增框个数


#  表格方式
class PersonInline(admin.TabularInline):
    model = Person  # 内嵌模型
extra = 1  # 新增框个数


@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    # 显示页数
    list_per_page = 5
    # 设置操作选项位置
    # actions_on_top = True
    # actions_on_bottom = True

    # 设置操作选项内容
    def my_action(self, request, queryset):
        pass
    # 给动作起名字
    my_action.short_description = "自定义操作"
    actions = ["my_action"]

    # 方法列
    def function_field(self, obj):
        return obj.area_name + "_方法列"
    # 给方法列设置名字
    function_field.short_description = "方法列"
    # 方法列设置排序
    function_field.admin_order_field = 'area_name'

    # 显示列
    list_display = ['id', 'area_name', 'area_code', 'function_field']

    # 右侧过滤器
    # list_filter = ['area_name']

    # 搜索框
    # search_fields = ['area_name', 'area_code']

    # 关联人员对象, 块方式关联
    inlines = [PersonInline]


# 注册模型类
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # 控制每页显示数据条数
    list_per_page = 5

    # 显示列
    list_display = ['id', 'person_name', 'person_age', 'person_sex', 'person_area']

    # 调整显示顺序
    # fields = ['person_name', 'person_sex', 'person_age', 'person_area']

    # 分组显示
    fieldsets = (
        ('基本选项', {'fields': ('person_name', 'person_sex')}),
        ('高级选项', {'fields': ('person_age', 'person_area')}),
    )