from django.conf.urls import url

from .views.category import *


urlpatterns = [
    url(r'^(?P<slug>\w+)/categories/$', CategoryListAPIView.as_view(), name="category-list"),
]
