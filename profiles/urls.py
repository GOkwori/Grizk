from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_reference>',
         views.order_history, name='order_history'),
]
