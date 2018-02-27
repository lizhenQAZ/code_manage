from django.db import models
from db.AbstractModel import AbstractModel


class Comment(AbstractModel):
    # 评论人
    name = models.CharField(max_length=100, verbose_name='评论人')
    # 邮箱
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    # 连接 http://www.name.com/
    link = models.URLField(blank=True, verbose_name='主页')
    # 内容
    content = models.TextField(blank=True, verbose_name='内容')
    # 添加表关联
    # 关联文章名
    post = models.ForeignKey('blog.Post', verbose_name='提交文章')

    def __unicode__(self):
        return self.content[:20]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-created_time']
