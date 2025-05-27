from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        
