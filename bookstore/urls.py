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
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from book import views


urlpatterns = [
      path('orders/', include('orders.urls')),
      path('books/', include('book.urls')),
      re_path(r'^delivery/$', TemplateView.as_view(template_name='delivery.html'), name="delivery"),
      re_path(r'^payments/$', TemplateView.as_view(template_name='payments.html'), name="payments"),
      re_path(r'^grafik-raboty/$', TemplateView.as_view(template_name='grafic.html'), name="grafik-raboty"),
      re_path(r'^returns/$', TemplateView.as_view(template_name='returns.html'), name="returns"),
      re_path(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
      path('admin/', admin.site.urls),
      path('', include('book.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \

