#coding=utf-8
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r"^$",views.queryAll),
    url(r"^page/(\d+)$",views.queryAll),
    url(r"^post/(\d+)$",views.detail),

]