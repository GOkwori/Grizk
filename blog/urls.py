from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('blog_dashboard/', views.blog_dashboard, name='blog_dashboard'),
]
