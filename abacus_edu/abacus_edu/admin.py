from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Video
from .models import Category
from .models import Application
from .filters import DropdownFilter


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'get_youtube_original_url_html_tag', 'is_recommended',)
    search_fields = ['title', ]
    fields = ('category', 'title', 'writer', 'youtube_id', 'description', 'is_recommended',)
    list_filter = (
        ('category__title', DropdownFilter),
        ('category__application__app_name', DropdownFilter),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', ]
    list_filter = (
        ('application__app_name', DropdownFilter),
    )


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'slug',)
    search_fields = ['app_name', ]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Application, ApplicationAdmin)
