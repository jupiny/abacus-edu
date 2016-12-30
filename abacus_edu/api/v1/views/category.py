from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView

from abacus_edu.models import Application
from api.v1.serializers.category import CategoryModelSerializer
from api.pagination import StandardResultsSetPagination


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        application = get_object_or_404(Application, slug=self.kwargs.get('application_slug'))
        return application.category_set.all()
