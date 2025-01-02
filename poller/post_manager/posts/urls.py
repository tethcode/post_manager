from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Show all posts
    path('<int:id>/', views.post_detail, name='post_detail'),  # Show a single post by ID
    path('<int:id>/', views.post_detail, name='post_detail'),  # View a single post
    path('create/', views.post_create, name='post_create'),  # Create a new post
    path('<int:id>/edit/', views.post_edit, name='post_edit'),  # Edit an existing post
    path('<int:id>/delete/', views.post_delete, name='post_delete'),
]
