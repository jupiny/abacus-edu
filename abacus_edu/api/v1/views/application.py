from rest_framework.generics import RetrieveAPIView

from api.v1.serializers.application import ApplicationModelSerializer
from api.mixins import ApplicationModelMixins


class ApplicationDetailAPIView(ApplicationModelMixins, RetrieveAPIView):
    serializer_class = ApplicationModelSerializer

    def get_object(self):
        application = self.get_application()
        return application
