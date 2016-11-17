from django.db import models
from django.utils.html import format_html


class Video(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="제목",
    )
    writer = models.CharField(
        max_length=30,
        verbose_name="작성자",
    )
    youtube_id = models.CharField(
        max_length=40,
        verbose_name="유튜브 ID",
    )

    def get_youtube_original_url(self):
        youtube_original_url = "https://www.youtube.com/watch?v={youtube_id}".format(
            youtube_id=self.youtube_id,
        )
        return format_html(
            "<a href='{}' target='_blank'>{}</a>",
            youtube_original_url,
            youtube_original_url,
        )
    get_youtube_original_url.short_description = "유투브 URL"

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"
