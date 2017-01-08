from django.db import models

from abacus_edu.behaviors import Timestampable


class Client(Timestampable, models.Model):
    application = models.ForeignKey(
        'Application',
        on_delete=models.CASCADE,
        verbose_name="어플리케이션",
    )
    token = models.TextField(
        verbose_name="토큰값",
    )
    like_video_set = models.ManyToManyField(
        'Video',
        related_name="liked_by_set",
    )

    def __str__(self):
        return self.token[:10]

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"
