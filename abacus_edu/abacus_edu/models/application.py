from django.db import models


class Application(models.Model):
    app_name = models.CharField(
        max_length=30,
        verbose_name="어플리케이션 이름",
        unique=True,
    )
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.app_name
