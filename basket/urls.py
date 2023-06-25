from django.urls import path

from basket import views

urlpatterns = [
    path('', views.all, name="basket")
]
