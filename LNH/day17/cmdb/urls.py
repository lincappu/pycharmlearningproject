from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    url(r'^host/$', views.host),
]
