from django.shortcuts import render

from basket.models import Basket


# Create your views here.
def all(request):
    basket = Basket.objects.all()
    return render(request, 'basket/basket.html', {"basket": basket})
