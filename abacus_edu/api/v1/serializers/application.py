from rest_framework import serializers

from abacus_edu.models import Application


class ApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('app_name', 'slug', 'representative_image_url', 'description',)
