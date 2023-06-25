from django.contrib import admin

from order.models import Order, OrderItem

# Register your models here.
admin.site.register(OrderItem)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'status')
