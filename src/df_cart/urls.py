from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)/$', views.add),     #add to cart  productid and count
    url(r'^edit(\d+)_(\d+)/$', views.edit),   #edit count of products -- product_id and count
    url(r'^delete(\d+)/$',views.delete),      #delete certain product of customer's cart
    url(r'^place_order/$',views.place_order),
]