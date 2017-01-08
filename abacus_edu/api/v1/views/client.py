from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from abacus_edu.models import Application


class ClientCheckTokenAPIView(APIView):

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_CLIENT_TOKEN')
        application = get_object_or_404(Application, slug=kwargs.get('application_slug'))
        application.client_set.get_or_create(token=token)
        return Response(status=status.HTTP_200_OK)
