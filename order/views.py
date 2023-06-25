from django.shortcuts import render

from order.models import Order


def all(request):
    orders = Order.objects.all()

    return render(request, 'order/orders.html', {'orders': orders })
