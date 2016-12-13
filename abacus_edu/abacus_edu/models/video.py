from django.db import models
from django.utils.html import format_html


class Video(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="카테고리",
    )

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
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def youtube_original_url(self):
        return "https://www.youtube.com/watch?v={youtube_id}".format(
            youtube_id=self.youtube_id,
        )

    def get_youtube_original_url_html_tag(self):
        return format_html(
            "<a href='{}' target='_blank'>{}</a>",
            self.youtube_original_url,
            self.youtube_original_url,
        )
    get_youtube_original_url_html_tag.short_description = "유투브 URL"

    @property
    def youtube_embed_url(self):
        return "https://www.youtube.com/embed/{youtube_id}".format(
            youtube_id=self.youtube_id,
        )

    def get_youtube_embed_url_html_tag(self):
        return format_html(
            "<iframe width='560' height='315' src='{}' frameborder='0' allowfullscreen></iframe>",
            self.youtube_embed_url,
        )
    get_youtube_embed_url_html_tag.short_description = "유투브 영상"

    @property
    def youtube_thumbnail_image_url(self):
        return "https://i.ytimg.com/vi/{youtube_id}/hqdefault.jpg".format(
            youtube_id=self.youtube_id,
        )

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"
