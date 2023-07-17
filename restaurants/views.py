from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm
from .forms import CommentForm
from .models import Restaurant
from .models import Comment

# RESTAURANT INDEX
def restaurant_index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant_index.html', context)

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

# SHOW RESTAURANT
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    comments = Comment.objects.filter(restaurant=restaurant)

    if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.restaurant = restaurant
                comment.save()
                return redirect('restaurant_detail', pk=pk)
    else:
        form = CommentForm(initial={'restaurant': restaurant.pk})

    context = {
        'restaurant': restaurant,
        'comments': comments,
        'form': form,
    }

    return render(request, 'restaurant_detail.html', context)

# UPDATE COMMENT
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=comment.restaurant.pk)
    else:
        form = RestaurantForm(instance=comment)
    return render(request, 'comment_update.html', {'form': form})

# DELETE COMMENT
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('restaurant_detail', pk=comment.restaurant.pk)

# RESTAURANT UPDATE
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
