from django.urls import path
from restaurants import views
from .views import restaurant_delete
from .views import restaurant_create
from .views import restaurant_update


urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path('restaurants/<int:pk>/delete/', restaurant_delete, name='restaurant_delete'),
    path('restaurants/<int:pk>/update/', restaurant_update, name='restaurant_update'),
    path('restaurants/create/', restaurant_create, name='restaurant_create'),
]
