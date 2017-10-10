from django.db import models


# 图书信息模型
class BookInfo(models.Model):

    # 图书标题
    book_title = models.CharField(max_length=50)
    # 图书评论量
    book_comment = models.IntegerField(default=0)
    # 图书阅读量
    book_read = models.IntegerField(default=0)
    # 图书是否删除
    book_delete = models.BooleanField(default=False)
    # 建立时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 上次修改时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title


# 英雄信息模型
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
    # 建立时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 上次修改时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hero_name

