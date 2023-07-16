from django.urls import path
from restaurants import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path('restaurants/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurants/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('restaurants/<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/update', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
] 
