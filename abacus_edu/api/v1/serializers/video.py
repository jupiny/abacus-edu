from rest_framework import serializers

from abacus_edu.models import Video


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'writer', 'youtube_id', 'get_youtube_original_url',
                  'get_youtube_thumbnail_image_url', 'get_youtube_embed_url',)
