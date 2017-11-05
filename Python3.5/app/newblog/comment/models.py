from django.db import models
from  db.AbstractModel import AbstractModel


class Comment(AbstractModel):
    # 评论人
    name = models.CharField(max_length=100)
    # 邮箱
    email = models.EmailField(max_length=255)
    # 连接 http://www.name.com/
    link = models.URLField(blank=True)
    # 内容
    content = models.TextField(blank=True)
    # 添加表关联
    # 关联文章名
    post = models.ForeignKey('blog.Post')

    def __unicode__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-created_time']
