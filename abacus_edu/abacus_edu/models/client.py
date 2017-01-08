from django.db import models

from abacus_edu.behaviors import Timestampable


class Client(Timestampable, models.Model):
    token = models.TextField(
        verbose_name="토큰값",
    )

    def __str__(self):
        return self.token[:10]

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"
