from datetime import datetime

from django.db import models

from abacus_edu.behaviors import Timestampable


class Category(Timestampable, models.Model):
    application = models.ForeignKey(
        'Application',
        on_delete=models.CASCADE,
        verbose_name="어플리케이션",
    )
    title = models.CharField(
        max_length=20,
        verbose_name="카테고리 제목",
    )
    publish_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="등록날짜(이 날짜 순으로 정렬됨. 미입력시 현재 날짜로 자동저장)",
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.publish_date:
            self.publish_date = datetime.now()
        super(Category, self).save(*args, **kwargs)

    @property
    def video_count(self):
        return self.video_set.count()

    @property
    def representative_image_url(self):
        if self.video_set.count():
            return self.video_set.first().youtube_thumbnail_image_url
        return self.application.representative_image.url

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        ordering = ['-publish_date', '-id']
