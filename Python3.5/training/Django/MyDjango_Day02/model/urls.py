from django.conf.urls import url
from .views import book, hero


urlpatterns = [
    url(r'^book/', book),
    url(r'^hero/(\d+)/$', hero),
]