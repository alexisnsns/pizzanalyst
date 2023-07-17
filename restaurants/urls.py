from django.urls import path
from restaurants import views

urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path('restaurants/create/', views.restaurant_create, name='restaurant_create'),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path('restaurants/<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('restaurants/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('comment/<int:pk>/update', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
