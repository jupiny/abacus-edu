from django.contrib import admin

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'get_youtube_original_url_html_tag',)
    search_fields = ['title', ]

admin.site.register(Video, VideoAdmin)
