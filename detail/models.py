from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", default="")
    image = models.ImageField(verbose_name="Фото", upload_to="img")
    weight = models.FloatField(verbose_name="Вес")
    price = models.IntegerField(verbose_name="Цена")
    in_stock = models.IntegerField(verbose_name="В наличии", default=0)
    sold = models.IntegerField(verbose_name="Продано", editable=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Детали'
        verbose_name = 'Деталь'
