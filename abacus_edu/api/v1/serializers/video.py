from rest_framework import serializers

from abacus_edu.models import Video


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'writer', 'youtube_id', 'youtube_original_url',
                  'youtube_thumbnail_image_url', 'youtube_embed_url',)
