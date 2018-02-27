from django.db import models
from tinymce.models import HTMLField


# 定义文件模型
class MyFile(models.Model):
    # upload_to参数没使用到
    file_name = models.ImageField(upload_to='deploy/')

    def __str__(self):
        return self.file_name


# 定义地区模型
class AreaInfo(models.Model):
    area_name = models.CharField(max_length=50, verbose_name='地区名')
    area_code = models.CharField(max_length=50, verbose_name='区号')

    def __str__(self):
        return self.area_name


# 定义人员模型
class Person(models.Model):
    person_name = models.CharField(max_length=30, verbose_name='名字')
    person_age = models.IntegerField(verbose_name='年龄')
    person_sex = models.CharField(max_length=5, verbose_name='性别')
    person_area = models.ForeignKey('AreaInfo', verbose_name='地区')

    def __str__(self):
        return self.person_name


# 定义城市模型
class City(models.Model):
    # 地区编码
    area_code = models.CharField(max_length=30)
    # 地区名称
    area_name = models.CharField(max_length=50)
    # 父级地区
    area_parent = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.area_name


# 定义富文本编辑器模型
class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_content = HTMLField()
