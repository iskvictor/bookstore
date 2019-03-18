"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1.4/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.urls import path, re_path

from . import views

app_name = 'orders'

urlpatterns = [
    re_path('^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path('^cart/$', views.cart, name='cart'),
    re_path('^checkout/$', views.checkout, name='checkout'),
    re_path('^remove_from_cart/$', views.remove_from_cart_view, name='remove_from_cart'),
    re_path('^count_cart/$', views.basket_count, name='basket_count'),
    re_path('^change_item_qty/$', views.change_item_qty, name='change_item_qty'),
    re_path('^order/$', views.order_create_view, name='create_order'),
    re_path('^make_order/$', views.make_order, name='make_order'),
]
