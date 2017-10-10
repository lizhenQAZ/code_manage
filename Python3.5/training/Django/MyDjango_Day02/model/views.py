from django.shortcuts import render
from .models import *


def book(request):
    bookinfos = BookInfo.objects.all()
    return render(request, "book.html", locals())


def hero(request, param):
    heroinfos = HeroInfo.objects.filter(hero_book_id=param)
    return render(request, "hero.html", locals())
