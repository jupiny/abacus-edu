from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'get_youtube_original_url_html_tag',)
    search_fields = ['title', ]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Video, VideoAdmin)
