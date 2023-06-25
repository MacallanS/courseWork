from django.contrib.auth.models import User
from django.db import models

from detail.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return f"{self.product.name} / {self.quantity}"


class Order(models.Model):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETE = 3
    STATUS_CHOICES = (
        (NEW, 'Получен'),
        (IN_PROGRESS, 'Собирается'),
        (COMPLETE, 'Готов к выдаче'),
    )

    def total_price(self):

        products = self.order_items.all().values_list('product_id',
                                                      'quantity')
        total = 0

        if products:
            for product in products:
                product_id = product[0]
                quantity = product[1]
                price = Product.objects.get(id=product_id).price

                total += quantity * price

        return total

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователи")
    status = models.IntegerField(choices=STATUS_CHOICES, default=NEW, verbose_name="Статус заказа")
    order_items = models.ManyToManyField(OrderItem, related_name="order_items", verbose_name="Позиции заказа")
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.created_at.date()} - {self.user}"
