from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
