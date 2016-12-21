from rest_framework import serializers

from abacus_edu.models import Category


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'video_count',)
