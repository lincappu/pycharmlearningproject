from django.conf.urls import url,include
from openstack import views
urlpatterns = [
    url(r'^host/$', views.host),
]
