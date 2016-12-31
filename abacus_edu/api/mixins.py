from rest_framework.response import Response


class CountResultsResponseMixins(object):

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = dict()
        response['count'] = queryset.count()
        response['results'] = serializer.data
        return Response(response)
