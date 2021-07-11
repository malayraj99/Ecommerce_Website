"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import home_page, about_page, contact_page, login_page, register_page
from django.urls import path
from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from products.views import ProductListView, ProductDetailView
#  ProductFeaturedListView, ProductFeaturedDetailView,  ProductDetailSlugView


urlpatterns = [
    re_path(r'^$', home_page),
    re_path(r'^about/$', about_page),
    re_path(r'^contact/$', contact_page),
    re_path(r'^login/$', login_page),
    re_path(r'^register/$', register_page),
    re_path(r'^products/', include("products.urls")),
    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
    # re_path(r'^featured/$', ProductFeaturedListView.as_view()),
    # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),


    # re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),


    # re_path(r'^products/$', include()),
    re_path(r'^admin/', admin.site.urls)
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)
