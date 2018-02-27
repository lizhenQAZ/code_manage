from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
import markdown
from .models import Post, Category, Tag
from comment.forms import CommentForm


# 定义首页链接
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1


# 定义文章详情页链接
class DetailInfoView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post_detail'

    def get(self, request, *args, **kwargs):
        response = super(DetailInfoView, self).get(request, *args, **kwargs)
        # 增加浏览量
        self.object.update_look()
        return response

    def get_object(self, queryset=None):
        post_detail = super(DetailInfoView, self).get_object(queryset=None)
        #     # 修改文章的显示样式
        #     post_detail.body = markdown.markdown(post_detail.body, extensions=[
        #         'markdown.extensions.extra',
        #         'markdown.extensions.codehilite',
        #         'markdown.extensions.toc',
        # ])
        #     return post_detail
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        post_detail.body = md.convert(post_detail.body)
        post_detail.toc = md.toc
        return post_detail

    def get_context_data(self, **kwargs):
        context = super(DetailInfoView, self).get_context_data(**kwargs)
        # 整理评论信息
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


# 定义归档链接
class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        return super(ArchiveView, self).get_queryset().filter(created_time__year=year, created_time__month=month, created_time__day=day)


# 定义分类链接
class CategoryView(IndexView):
    def get_queryset(self):
        cag = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(cag=cag)


# 定义标签视图
class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=tag)
