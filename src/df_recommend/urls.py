from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^list/$', views.list, name='list'),
    url(r'^all(\d+)_(\d+)_(\d+)/$', views.list, name='list'),      
    url(r'^(\d+)/$', views.detail, name='detail'),    
    url(r'^search/$',MySearchView()),
]
