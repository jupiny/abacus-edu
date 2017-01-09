from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from api.v1.serializers.video import VideoModelSerializer
from api.mixins import CountResultsResponseMixins, ClientModelMixins


class ClientCheckTokenAPIView(ClientModelMixins, APIView):

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_CLIENT_TOKEN')
        application = self.get_application()
        application.client_set.get_or_create(token=token)
        return Response(status=status.HTTP_200_OK)


class ClientRenewTokenAPIView(ClientModelMixins, APIView):

    def get(self, request, *args, **kwargs):
        new_token = request.META.get('HTTP_NEW_CLIENT_TOKEN')
        client = self.get_client()
        client.token = new_token
        client.save()
        return Response(status=status.HTTP_200_OK)


class ClientLikeVideoListCreateAPIView(ClientModelMixins, CountResultsResponseMixins, ListCreateAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        client = self.get_client()
        return client.like_video_set.all()

    def create(self, request, *args, **kwargs):
        client = self.get_client()
        video_ids = self.request.data.getlist('video_id')
        video_ids = map(lambda x: int(x), video_ids)
        cur_like_video_ids = client.like_video_set.values_list('id', flat=True)
        new_video_ids = list(set(video_ids)-set(cur_like_video_ids))
        client.like_video_set.add(*new_video_ids)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        client = self.get_client()
        video_ids = self.request.data.getlist('video_id')
        client.like_video_set.remove(*video_ids)
        return Response(status=status.HTTP_204_NO_CONTENT)
