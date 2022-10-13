# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from django.urls import path,re_path
from . import views

app_name='polls'
urlpatterns=[
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),

	# 下面是额外添加的测试,re_path 最好使用命名组语法
	# path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
	#
	# re_path('articles/2003/', views.special_case_2003),
	# re_path(r'^articles/(?p<year>[0-9]{4}/$)')

]
