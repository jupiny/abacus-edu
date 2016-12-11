from rest_framework.generics import ListAPIView

from abacus_edu.models import Application
from api.v1.serializers.video import VideoModelSerializer


class VideoListAPIView(ListAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        application = Application.objects.get(slug=self.kwargs.get('slug'))
        category = application.category_set.get(pk=self.kwargs.get('pk'))
        return category.video_set.all()
