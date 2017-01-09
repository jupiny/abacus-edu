from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from abacus_edu.models import Application, Category, Video, Client


class CountResultsResponseMixins(object):

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = dict()
        response['count'] = queryset.count()
        response['results'] = serializer.data
        return Response(response)


class ApplicationModelMixins(object):

    def get_application(self):
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        return application


class CategoryModelMixins(ApplicationModelMixins):

    def get_category(self):
        application = self.get_application()
        category = get_object_or_404(application.category_set, pk=self.kwargs.get('category_id'))
        return category


class VideoModelMixins(CategoryModelMixins):

    def get_video(self):
        category = self.get_category()
        video = get_object_or_404(category.video_set, pk=self.kwargs.get('video_id'))
        return video


class ClientModelMixins(ApplicationModelMixins):

    def get_client(self):
        application = self.get_application()
        token = self.request.META.get('HTTP_CLIENT_TOKEN')
        client = get_object_or_404(application.client_set, token=token)
        return client
