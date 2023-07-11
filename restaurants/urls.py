from django.urls import path
from restaurants import views

urlpatterns = [

    path("", views.restaurant_index, name="restaurant_index"),

    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),

]
