from django.shortcuts import render
from restaurants.models import Restaurant

# Create your views here.
def restaurants(request):
    return render(request, 'restaurants.html', {})

def restaurant_index(request):

    restaurants = Restaurant.objects.all()

    context = {

        'restaurants': restaurants

    }

    return render(request, 'restaurant_index.html', context)


def restaurant_detail(request, pk):

    restaurant = Restaurant.objects.get(pk=pk)

    context = {

        'restaurant': restaurant

    }

    return render(request, 'restaurant_detail.html', context)
