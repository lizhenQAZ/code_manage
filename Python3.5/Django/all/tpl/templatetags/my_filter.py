from django.template import Library


register = Library()


@register.filter("mod")
def my_mod(param):
    return param % 2
