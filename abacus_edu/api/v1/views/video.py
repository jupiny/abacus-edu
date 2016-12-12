from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView

from abacus_edu.models import Application, Category
from api.v1.serializers.video import VideoModelSerializer


class VideoListAPIView(ListAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        application = get_object_or_404(Application, slug=self.kwargs.get('slug'))
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return category.video_set.all()
