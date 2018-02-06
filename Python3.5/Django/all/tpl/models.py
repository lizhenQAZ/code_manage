from django.db import models
from db.AbstractModel import AbstractModel


# 创建留言板模型
class Message(AbstractModel):
    # 留言姓名
    mess_username = models.CharField(max_length=30)
    # 留言内容
    mess_content = models.CharField(max_length=1000)
