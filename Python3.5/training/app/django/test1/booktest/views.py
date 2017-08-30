from django.shortcuts import render
from booktest.models import BookInfo


def index(reqeust):
    booklist = BookInfo.objects.all()
    return render(reqeust, 'booktest/index.html', {'booklist': booklist})


def detail(reqeust, id):
    book = BookInfo.objects.get(pk=id)
    return render(reqeust, 'booktest/detail.html', {'book': book})
