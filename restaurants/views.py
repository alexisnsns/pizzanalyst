from django.shortcuts import render
from restaurants.models import Restaurant
from .forms import RestaurantForm

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

# Create your views here.
def restaurants(request):
    return render(request, 'restaurants.html', {})


# CREATE
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_index')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_create.html', {'form': form})


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

# DELETE
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return redirect('restaurant_index')
