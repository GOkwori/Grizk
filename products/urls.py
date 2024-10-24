from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
