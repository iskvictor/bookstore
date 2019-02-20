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


app_name ="book"


urlpatterns = [
    re_path(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.CategoryDetailView.as_view(), name='list_category'),
    re_path(r'^$', views.BookListView.as_view(), name="book_list")

]
