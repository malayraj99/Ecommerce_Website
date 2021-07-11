
from django.urls import path, re_path
from django.conf.urls import url, include

from .views import ProductListView, ProductDetailView


urlpatterns = [
    
    re_path(r'^$', ProductListView.as_view()),
    
    re_path(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),

    
]
