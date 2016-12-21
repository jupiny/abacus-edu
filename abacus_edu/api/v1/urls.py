from django.conf.urls import url

from .views.category import *
from .views.video import *


urlpatterns = [
    url(r'^(?P<application_slug>\w+)/categories/$',
        CategoryListAPIView.as_view(),
        name="category-list"),
    url(r'^(?P<application_slug>\w+)/categories/(?P<category_id>\d+)/videos/$',
        VideoListAPIView.as_view(),
        name="video-list"),
    url(r'^(?P<application_slug>\w+)/categories/(?P<category_id>\d+)/videos/(?P<video_id>\d+)/$',
        VideoDetailAPIView.as_view(),
        name="video-detail"),
    url(r'^(?P<application_slug>\w+)/recommended-videos/$',
        RecommendedVideoListAPIView.as_view(),
        name="recommended-video-list"),
]
