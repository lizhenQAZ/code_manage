from django.db import models
from db.AbstractModel import AbstractModel
from tinymce.models import HTMLField


class Category(AbstractModel):
    # 商品类别
    cag_name = models.CharField(max_length=30)


class GoodsInfoManager(models.Manager):
    # 获取最热的三个商品
    def get_hot_by_cag(self, cag):
        return self.filter(goods_cag=cag).order_by('-goods_look')[:3]

    # 获取最新的四个商品
    def get_new_by_cag(self, cag):
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    # 获取所有商品中最热的两个商品
    def get_hot_by_all(self):
        return self.all().order_by('-goods_look')[:2]


class GoodsInfo(AbstractModel):
    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品价格
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品单位
    goods_unit = models.CharField(max_length=10)
    # 商品上架
    goods_status = models.BooleanField(default=True)
    # 商品图片
    goods_image = models.ImageField()
    # 商品简述
    goods_brief = models.CharField(max_length=100)
    # 商品描述
    goods_desc = HTMLField()
    # 商品浏览量
    goods_look = models.IntegerField(default=0)
    # 商品销量
    goods_sales = models.IntegerField(default=0)
    # 商品类别
    goods_cag = models.ForeignKey(Category)

    objects = GoodsInfoManager()


# 创建广告模型
class Advertisement(AbstractModel):
    # 广告位名称
    ad_name = models.CharField(max_length=30)
    # 广告位图片
    ad_image = models.ImageField(upload_to='ad/')
    # 广告位链接
    ad_link = models.CharField(max_length=80)
