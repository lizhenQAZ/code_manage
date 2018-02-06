from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^center/$', center, name='center'),
    url(r'^add/(.+)/$', add, name='add'),
    url(r'^del/(.+)/$', delete, name='delete'),
    url(r'^update/(.+)/$', update, name='update'),
]
