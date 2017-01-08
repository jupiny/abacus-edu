from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from abacus_edu.models import Application, Client
from api.v1.serializers.video import VideoModelSerializer
from api.mixins import CountResultsResponseMixins


class ClientCheckTokenAPIView(APIView):

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_CLIENT_TOKEN')
        application = get_object_or_404(Application, slug=kwargs.get('application_slug'))
        application.client_set.get_or_create(token=token)
        return Response(status=status.HTTP_200_OK)


class ClientLikeVideoListCreateAPIView(CountResultsResponseMixins, ListCreateAPIView):
    serializer_class = VideoModelSerializer

    def get_queryset(self):
        token = self.request.META.get('HTTP_CLIENT_TOKEN')
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        client = get_object_or_404(Client, token=token)
        return client.like_video_set.all()

    def create(self, request, *args, **kwargs):
        token = self.request.META.get('HTTP_CLIENT_TOKEN')
        video_ids = request.data.getlist('video_id')
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        client = get_object_or_404(Client, token=token)
        client.like_video_set.add(*video_ids)
        return Response(status=status.HTTP_201_CREATED)
