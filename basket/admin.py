from django.contrib import admin

from basket.models import Basket, BasketItem

# Register your models here.
admin.site.register(BasketItem)


@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
    list_display = ('user', 'add_datetime', 'total_price')
