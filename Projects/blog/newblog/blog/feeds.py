# coding: utf-8
from django.contrib.syndication.views import Feed
from .models import Post
from django.shortcuts import reverse


class AllPostsRssFeed(Feed):
    title = "网站文章展示"
    link = "/"
    description = "网站描述信息"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return "[{}] {}".format(item.cag, item.title)

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse("blog:detail", kwargs={'pk': item.pk})

