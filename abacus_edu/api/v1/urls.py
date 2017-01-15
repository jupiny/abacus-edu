from django.conf.urls import url

from .views.application import *
from .views.category import *
from .views.video import *
from .views.client import *


urlpatterns = [
    url(r'^(?P<application_slug>\w+)/$',
        ApplicationDetailAPIView.as_view(),
        name="application-detail"),
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
    url(r'^(?P<application_slug>\w+)/categories/(?P<category_id>\d+)/video-youtube-ids/$',
        VideoYoutubeIDListAPIView.as_view(),
        name="video-youtube-id-list"),
    url(r'^(?P<application_slug>\w+)/check-token/$',
        ClientCheckTokenAPIView.as_view(),
        name="check-token"),
    url(r'^(?P<application_slug>\w+)/renew-token/$',
        ClientRenewTokenAPIView.as_view(),
        name="renew-token"),
    url(r'^(?P<application_slug>\w+)/like-videos/$',
        ClientLikeVideoListCreateAPIView.as_view(),
        name="like-video-list"),
]
