from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name="제목",
    )
