from django.urls import path

from detail import views

urlpatterns = [
    path('', views.get_all_products, name='products'),
    path('categories/', views.get_all_categories, name='categories'),

]
