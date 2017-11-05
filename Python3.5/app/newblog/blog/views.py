from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Category
import markdown
from comment.forms import CommentForm


# 定义首页链接
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', locals())


# 定义文章详情页链接
def detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    post_detail.body = markdown.markdown(post_detail.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # 整理评论信息
    form = CommentForm()
    comment_list = post_detail.comment_set.all()
    return render(request, 'blog/detail.html', locals())


# 定义归档链接
def archives(request, year, month, day):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    created_time__day=day
                                    )
    return render(request, 'blog/index.html', context=locals())


# 定义分类链接
def category(request, pk):
    cag = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(cag=cag)
    return render(request, 'blog/index.html', context=locals())
