from django.contrib.auth.models import User
from django.db import models

from detail.models import Product


# Create your models here.
class BasketItem(models.Model):
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Позиция корзины"
        verbose_name_plural = "Позиции корзины"

    def __str__(self):
        return f"{self.product.name} / {self.quantity}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователи")
    entries = models.ManyToManyField(BasketItem, verbose_name="Позиции")
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)

    def total_price(self):

        products = self.entries.all().values_list('product_id',
                                                  'quantity')
        total = 0

        if products:
            for product in products:
                product_id = product[0]
                quantity = product[1]
                price = Product.objects.get(id=product_id).price

                total += quantity * price

        return total

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"{self.add_datetime.date() } - {self.user}"
