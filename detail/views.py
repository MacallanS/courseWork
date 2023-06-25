from django.shortcuts import render

from detail.models import Product, Category


def get_all_products(request):
    products = Product.objects.all()
    return render(request, "detail/detail.html", {"products": products})


def get_all_categories(request):
    categories = Category.objects.all()
    return render(request, "categories/categories.html", {"categories": categories})
