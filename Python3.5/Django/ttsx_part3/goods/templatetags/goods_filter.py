#-*-coding:utf-8-*-
from django.template import Library


register = Library()


@register.filter
def create_image(index):
    print(index)
    return 'images/banner0' + str(index) + '.jpg'
