from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.post_index, name = 'post_index'),
    path('posts/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('my_posts/', views.my_posts, name = 'my_posts'),
    path('new_post/', views.new_post, name = 'new_post'),
    path('edit_post/<int:pk>/', views.edit_post, name = 'edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name = 'delete_post'),
    path('register/', views.register, name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
]