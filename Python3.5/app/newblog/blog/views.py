from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Category
import markdown
from comment.forms import CommentForm
from django.views.generic import ListView, DetailView


# 定义首页链接
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


# 定义文章详情页链接
class DetailInfoView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post_detail'
    def get(self, request, *args, **kwargs):
        response

    post_detail = get_object_or_404(Post, pk=pk)
    post_detail.body = markdown.markdown(post_detail.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # 整理评论信息
    form = CommentForm()
    comment_list = post_detail.comment_set.all()



# 定义归档链接
class ArchiveClass(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        return super(ArchiveClass, self).get_queryset().filter(created_time__year=year, created_time__month=month, created_time__day=day)


# 定义分类链接
class CategoryView(IndexView):
    def get_queryset(self):
        cag = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(cag=cag)
