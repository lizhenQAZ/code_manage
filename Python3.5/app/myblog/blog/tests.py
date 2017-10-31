from django.test import TestCase
from blog.models import Category, Tag, Post
from django.contrib.auth.models import User


# # 创建测试数据
# c = Category(name='category_test')
# c.save()
# t = Tag(name='tag_test')
# t.save()
# user = User.objects.get(username='user_test')
# c = Category.objects.get(name='category_test')
# p = Post(title='title_test', body='body_test', category=c, author=user)
# p.save()


# 查询测试数据
print(Category.objects.all())
print(Tag.objects.all())
print(Post.objects.all())
for item in Post.objects.all():
    print(item.category.name)
print(Post.objects.get(title='title_test'))
