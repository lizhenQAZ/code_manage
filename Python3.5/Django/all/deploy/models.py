from django.db import models
# 引入富文本模型类
from tinymce.models import HTMLField
# 引入公共模型类
from db.AbstractModel import AbstractModel


# 文件模型
class MyFile(AbstractModel):
    # upload_to参数没使用到
    file_name = models.ImageField(upload_to='deploy/')

    def __str__(self):
        return self.file_name


# 地区模型
class AreaInfo(AbstractModel):
    area_name = models.CharField(max_length=50, verbose_name='地区名')
    area_code = models.CharField(max_length=50, verbose_name='区号')

    def __str__(self):
        return self.area_name


# 城市模型
class City(AbstractModel):
    # 地区编码
    area_code = models.CharField(max_length=30)
    # 地区名称
    area_name = models.CharField(max_length=50)
    # 父级地区
    area_parent = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.area_name


# 富文本编辑器模型
class News(AbstractModel):
    news_title = models.CharField(max_length=50)
    news_content = HTMLField()


# 人员模型
class Person(AbstractModel):
    person_name = models.CharField(max_length=30, verbose_name='名字')
    person_age = models.IntegerField(verbose_name='年龄')
    person_sex = models.CharField(max_length=5, verbose_name='性别')
    person_area = models.ForeignKey('AreaInfo', verbose_name='地区')

    def __str__(self):
        return self.person_name
