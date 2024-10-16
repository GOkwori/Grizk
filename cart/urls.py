from django.contrib import admin
from django.urls import path
from . import views

# URL patterns for the cart application
urlpatterns = [
    # URL to view the cart page
    path('', views.view_cart, name='view_cart'),

    # URL to add an item to the cart
    # Expects an item ID to specify which product to add
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),

    # URL to adjust the quantity of an item in the cart
    # Expects an item ID to identify which product to adjust
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),

    # URL to remove an item from the cart
    # Expects an item ID to specify which product to remove
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
