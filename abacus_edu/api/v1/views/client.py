from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from api.v1.serializers.video import VideoModelSerializer
from api.mixins import CountResultsResponseMixins, ClientModelMixins


class ClientCheckTokenAPIView(APIView):

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_CLIENT_TOKEN')
        application = get_object_or_404(Application, slug=kwargs.get('application_slug'))
        application.client_set.get_or_create(token=token)
        return Response(status=status.HTTP_200_OK)


class ClientLikeVideoListCreateAPIView(ClientModelMixins, CountResultsResponseMixins, ListCreateAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        client = self.get_client()
        return client.like_video_set.all()

    def create(self, request, *args, **kwargs):
        client = self.get_client()
        video_ids = self.request.data.getlist('video_id')
        client.like_video_set.add(*video_ids)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        client = self.get_client()
        video_ids = self.request.data.getlist('video_id')
        client.like_video_set.remove(*video_ids)
        return Response(status=status.HTTP_204_NO_CONTENT)
