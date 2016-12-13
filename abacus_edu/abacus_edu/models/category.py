from django.db import models


class Category(models.Model):
    application = models.ForeignKey(
        'Application',
        on_delete=models.CASCADE,
        verbose_name="어플리케이션",
    )
    title = models.CharField(
        max_length=20,
        verbose_name="카테고리 제목",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
