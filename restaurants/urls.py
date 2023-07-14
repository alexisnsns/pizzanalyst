from django.urls import path
from restaurants import views

urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path('restaurants/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurants/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('restaurants/<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:restaurant_pk>/comment/<int:pk>/update', views.comment_update, name='comment_update'),
    path('<int:restaurant_pk>/comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),

]
