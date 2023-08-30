from django.urls import path
from restaurants import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path('create/', views.restaurant_create, name='restaurant_create'),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path('<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('comment/<int:pk>/update', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('results/', views.SearchView.as_view(), name='search'),
]
