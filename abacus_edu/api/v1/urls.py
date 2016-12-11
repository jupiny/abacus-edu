from django.conf.urls import url

from .views.category import *
from .views.video import *


urlpatterns = [
    url(r'^(?P<slug>\w+)/categories/$', CategoryListAPIView.as_view(), name="category-list"),
    url(r'^(?P<slug>\w+)/categories/(?P<pk>\d+)/videos/$', VideoListAPIView.as_view(), name="video-list"),
]
