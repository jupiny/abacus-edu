from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.serializers.video import VideoModelSerializer, VideoYoutubeIDSerializer
from api.pagination import StandardResultsSetPagination
from api.mixins import CountResultsResponseMixins, ApplicationModelMixins, CategoryModelMixins, VideoModelMixins

from abacus_edu.models import Video


class VideoListAPIView(CategoryModelMixins, ListAPIView):
    serializer_class = VideoModelSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        category = self.get_category()
        return category.video_set.all()


class VideoDetailAPIView(VideoModelMixins, RetrieveAPIView):
    serializer_class = VideoModelSerializer

    def get_object(self):
        video = self.get_video()
        return video


class RecommendedVideoListAPIView(ApplicationModelMixins, CountResultsResponseMixins, ListAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        application = self.get_application()
        return Video.objects.filter(category__application=application, is_recommended=True)


class VideoYoutubeIDListAPIView(CategoryModelMixins, CountResultsResponseMixins, ListAPIView):
    serializer_class = VideoYoutubeIDSerializer

    def get_queryset(self):
        category = self.get_category()
        return category.video_set.all()
