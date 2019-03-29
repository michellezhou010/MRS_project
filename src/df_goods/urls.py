from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^list/$', views.list, name='list'),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),      # d+ typeid with page index and sort info 
    url(r'^(\d+)/$', views.detail, name='detail'),     # details
    url(r'^search/$',MySearchView()),
]
