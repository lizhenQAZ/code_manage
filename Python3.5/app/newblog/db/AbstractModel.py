# -*- coding: utf-8 -*-
from django.db import models


class AbstractModel(models.Model):
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 修改时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        abstract = True
