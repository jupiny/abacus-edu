from django.contrib import admin

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'writer', 'youtube_id', 'get_youtube_original_url',)
    readonly_fields = ('get_youtube_original_url',)
    list_display = ('title', 'writer', 'get_youtube_original_url',)
    search_fields = ['title', ]

admin.site.register(Video, VideoAdmin)
