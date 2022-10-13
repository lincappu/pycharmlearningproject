"""day17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls.py import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls.py'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

# http://127.0.0.1:8000/cmdb/host/
# http://127.0.0.1:8000/openstack/host/
urlpatterns = [
    # url(r'^admin/', admin.site.urls.py),
    url(r'^test/$', views.test),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^parts/$', views.parts),
    url(r'^part_add/$', views.part_add),
    url(r'^part_del/$', views.part_del),
    url(r'^part_edit/$', views.part_edit),

    url(r'^example/$', views.example),

    url(r'^example/add/$', views.example_add),
    url(r'^example_edit/(?P<xid>\d+)/(?P<nid>\d+)/$', views.example_edit),
    url(r'^keng/$', views.keng),
    url(r'^tpl/$', views.tpl),


    url(r'^cmdb/', include('cmdb.urls.py')),
    url(r'^openstack/', include('openstack.urls.py')),

]
