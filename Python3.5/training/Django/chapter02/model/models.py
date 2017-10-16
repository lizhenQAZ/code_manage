from django.db import models


# 一对多模型
class BookInfo(models.Model):
    # 图书标题
    book_title = models.CharField(max_length=50)
    # 图书评论量
    book_comment = models.IntegerField(default=0)
    # 图书阅读量
    book_read = models.IntegerField(default=0)
    # 图书是否删除
    book_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title


class HeroInfo(models.Model):
    # 英雄名字
    hero_name = models.CharField(max_length=50)
    # 英雄性别
    hero_sex = models.BooleanField(default=True)
    # 英雄描述
    hero_desc = models.TextField()
    # 英雄是否删除
    hero_delete = models.BooleanField(default=False)
    # 英雄所属图书
    hero_book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hero_name

    class Meta:
        ordering = ['id']


# 一对一模型
class Place(models.Model):
    # 地点名字
    place_name = models.CharField(max_length=50)
    # 详细地址
    place_address = models.CharField(max_length=80)

    def __str__(self):
        return self.place_name


class Restaurant(models.Model):
    # 饭店名字
    res_name = models.CharField(max_length=100)
    # 饭店地点
    res_place = models.OneToOneField(Place)

    def __str__(self):
        return self.res_name


# 自定义模型表名
class NewPlace(models.Model):
    # 地点名字
    place_name = models.CharField(max_length=50)
    # 详细地址
    place_address = models.CharField(max_length=80)

    class Meta:
        db_table = "my_custom_place"

    def __str__(self):
        return self.place_name


# 自定义抽象模型
class Person(models.Model):
    gender = models.BooleanField(default=False)
    age = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Student(Person):
    activity = models.CharField(max_length=50)


# 自定义模型所有类型
class Superman(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False)
    gender = models.NullBooleanField(default=False)
    desc = models.CharField(max_length=200, db_column='description')
    message = models.TextField(max_length=1000)
    age = models.IntegerField(default=0)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    profile = models.FileField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)


# 自定义非级联删除
# 一对多模型
class Dormitory(models.Model):
    # 寝室名字
    dormitory_name = models.CharField(max_length=50)

    def __str__(self):
        return self.book_title


class Member(models.Model):
    # 人员名字
    member_name = models.CharField(max_length=50)
    # 人员所属寝室
    member_dormitory = models.ForeignKey(Dormitory, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.member_name


# 自定义和修改管理器类
class BookDescManager(models.Manager):
    def with_new_name(self):
        books = super(BookDescManager, self).all()
        for book in books:
            book.book_title = "书名_" + book.book_title
        return books

    def all(self):
        return super(BookDescManager, self).all().filter(book_isdelete=False)


# 定义图书模型类BookDesc
class BookDesc(models.Model):
    book_title = models.CharField(max_length=20)  # 图书名称
    book_read = models.IntegerField(default=0)  # 阅读量
    book_comment = models.IntegerField(default=0)  # 评论量
    book_isdelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):
        return self.book_title

    objects = BookDescManager()


# 自定义自关联
# 创建地区模型
class AreaInfo(models.Model):
    # 地区名称
    area_name = models.CharField(max_length=30)
    # 父级地区
    area_parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.area_name
