from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from blog.models import Post
from .forms import CommentForm


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:detail', kwargs={'pk': pk}), context=locals())
        else:
            comment_list = post.comment_set.all()
            return redirect(reverse('blog:detail', kwargs={'pk': pk}), context=locals())
    return redirect(reverse('blog:detail', kwargs={'pk': pk}), context=locals())
