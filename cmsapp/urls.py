# cms/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_content, name='create_content'),
    path('view/<int:pk>/', views.view_content, name='view_content'),
    path('edit/<int:pk>/', views.edit_content, name='edit_content'),
    path('delete/<int:pk>/', views.delete_content, name='delete_content'),
    # Add more URL patterns for content management endpoints as needed
]
