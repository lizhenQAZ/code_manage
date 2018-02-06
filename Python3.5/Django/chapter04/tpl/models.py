from django.db import models


# 创建留言板模型
class Message(models.Model):
    # 留言姓名
    mess_username = models.CharField(max_length=30)
    # 留言内容
    mess_content = models.CharField(max_length=1000)
    # 留言时间
    mess_datetime = models.DateTimeField(auto_now_add=True)
