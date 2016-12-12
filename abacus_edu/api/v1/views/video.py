from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView

from abacus_edu.models import Application, Category, Video
from api.v1.serializers.video import VideoModelSerializer


class VideoListAPIView(ListAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        category = get_object_or_404(Category, pk=self.kwargs.get('category_id'))
        return category.video_set.all()


class VideoDetailAPIView(RetrieveAPIView):
    serializer_class = VideoModelSerializer

    def get_object(self):
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        category = get_object_or_404(Category, pk=self.kwargs.get('category_id'))
        video = get_object_or_404(Video, pk=self.kwargs.get('video_id'))
        return video