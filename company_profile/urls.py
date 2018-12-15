from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='loginpage'),
    url(r'^homepage/', views.index, name='homepage'),
    url(r'^manager/', views.manager, name='manager_view'),
    url(r'^other/(?P<x>\d+)/', views.other, name='other_view'),
    url(r'^customer/(?P<x>\d+)/', views.customer, name='customer_view'),

]