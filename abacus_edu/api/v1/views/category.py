from rest_framework.generics import ListAPIView

from abacus_edu.models import Application
from api.v1.serializers.category import CategoryModelSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        application = Application.objects.get(slug=self.kwargs.get('slug'))
        return application.category_set.all()
