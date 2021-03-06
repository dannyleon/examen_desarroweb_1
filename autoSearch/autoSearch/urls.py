"""autoSearch URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from carros import views

from django.conf import settings
from django.conf.urls.static import static

from carros.views import carlist, cardetail,CarCreateView,CarListView,CarUpdateView,CarDeleteView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home.html'),

    url(r'^carlist$',carlist.as_view(), name = 'CarList'),

    url(r'^cars/create$', CarCreateView.as_view(), name='CarCreate'),

    url(r'^cars/listc/$', CarListView.as_view(), name='car_list'),

    url(r'^cardetail/(?P<pk>[0-9]+)/$', cardetail.as_view(),name= 'CarDetail'),

    url(r'^cardetail/(?P<pk>[0-9]+)/edit/$', CarUpdateView.as_view(),name= 'CarEdit'),

    url(r'^cardetail/(?P<pk>[0-9]+)/delete/$', CarDeleteView.as_view(),name= 'CarDelete'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
