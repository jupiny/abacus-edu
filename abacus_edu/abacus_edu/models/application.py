import os
import datetime

from django.db import models

from abacus_edu.behaviors import Timestampable


def set_filename_format(filename):
    now = datetime.datetime.now()
    return "{filename}-{date}-{microsecond}{extension}".format(
        filename=filename,
        date=now.date().strftime("%Y-%m-%d"),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def get_representative_image_path(instance, filename):
    now = datetime.datetime.now()
    path = "representative_image/{app_name}/{filename}".format(
        app_name=instance.app_name,
        filename=set_filename_format(filename),
    )
    return path


class Application(Timestampable, models.Model):
    app_name = models.CharField(
        max_length=30,
        verbose_name="어플리케이션 이름",
        unique=True,
    )
    slug = models.SlugField(
        max_length=30,
        verbose_name="Slug (URL로 사용됨)",
        unique=True,
    )
    representative_image = models.ImageField(
        upload_to=get_representative_image_path,
        blank=True,
        verbose_name="대표 이미지 (유튜브 영상이 링크가 안 될때 보여주는 이미지)",
    )
    description = models.TextField(
        blank=True,
        verbose_name="설명 (어플의 회색 부분에 출력됨)",
    )

    def __str__(self):
        return self.app_name

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Application"

    @property
    def representative_image_url(self):
        return self.representative_image.url
