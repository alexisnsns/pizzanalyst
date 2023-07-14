from django.shortcuts import render
from restaurants.models import Restaurant
from .forms import RestaurantForm
from .forms import CommentForm
from .models import Restaurant

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

# Create your views here.
def restaurants(request):
    return render(request, 'restaurants.html', {})


# CREATE RESTAURANT
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_index')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_create.html', {'form': form})


# CREATE COMMENT
def comment_create(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.restaurant = restaurant
            comment.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = CommentForm(instance=restaurant)
    return render(request, 'comment_create.html', {'form': form})

# READ
def restaurant_index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant_index.html', context)

# SHOW
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant
    }
    return render(request, 'restaurant_detail.html', context)

# UPDATE
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_update.html', {'form': form})

# DELETE
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return redirect('restaurant_index')
