from django.conf.urls import url
from .views import *
from MyDjangoStock import settings

urlpatterns = [
    url(r'^$', index),
    url(r'^index\.html$', index),
    url(r'^center\.html$', center),
    url(r'^add/(.+)\.html$', add),
    url(r'^del/(.+).\html$', delete),
    url(r'^update/(.+)\.html$', update),
    url(r'^update/(.+)/(.+)\.html$', update_new),
    url(r'^static/.*$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
]