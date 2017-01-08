from rest_framework.generics import ListAPIView

from api.v1.serializers.category import CategoryModelSerializer
from api.pagination import StandardResultsSetPagination
from api.mixins import ApplicationModelMixins


class CategoryListAPIView(ApplicationModelMixins, ListAPIView):
    serializer_class = CategoryModelSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        application = self.get_application()
        return application.category_set.all()
