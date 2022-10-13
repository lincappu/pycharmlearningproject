# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from django.urls import path

from . import views

app_name='testone'
urlpatterns = [
    path('', views.index, name='index'),
]