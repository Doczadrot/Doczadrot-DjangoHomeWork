from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    contents = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    preview = models.ImageField(upload_to="blog_images/", verbose_name="Изображение", blank=True, null=True)
    on_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров' )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title"]
