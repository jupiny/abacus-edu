from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name="제목",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
