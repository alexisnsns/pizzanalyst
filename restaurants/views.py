from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm
from .forms import CommentForm
from .models import Restaurant
from .models import Comment
from django.contrib.auth.decorators import login_required, permission_required
from environ import Env
from django.views.generic import ListView

# RESTAURANT INDEX
def restaurant_index(request):
    restaurants = Restaurant.objects.all().order_by('name')
    restaurants_addresses = [restaurant.address for restaurant in restaurants]
    restaurants_names = [restaurant.name.capitalize() for restaurant in restaurants]
    restaurants_indexes = [restaurant.id for restaurant in restaurants]

    env = Env()
    env.read_env()

    context = {
        'restaurants': restaurants,
        'restaurants_addresses': restaurants_addresses,
        'restaurants_names': restaurants_names,
        'restaurants_indexes': restaurants_indexes,

        'MAPBOX_ACCESS_TOKEN': env('MAPBOX_ACCESS_TOKEN')

    }
    return render(request, 'restaurant_index.html', context)




class SearchView(ListView):
    model = Restaurant
    template_name = 'restaurant_index.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Restaurant.objects.filter(name__contains=query)
          result = postresult
       else:
           result = Restaurant.objects.all()
       return result

    def get_context_data(self, **kwargs):
        env = Env()
        env.read_env()
        context = super().get_context_data(**kwargs)
        context['MAPBOX_ACCESS_TOKEN'] = env('MAPBOX_ACCESS_TOKEN')
        context['restaurants'] = Restaurant.objects.all()
        context['restaurants_addresses'] = [restaurant.address for restaurant in context['restaurants']]
        context['restaurants_names'] = [restaurant.name.capitalize() for restaurant in context['restaurants']]
        context['restaurants_indexes'] = [restaurant.id for restaurant in context['restaurants']]

        return context

    def render_to_response(self, context, **response_kwargs):
        return self.response_class(
            request=self.request,
            template=self.template_name,
            context=context,
            **response_kwargs
        )


# RESTAURANT CREATE
@login_required
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.address = restaurant.address.replace(",", "")
            restaurant.created_by = request.user
            restaurant.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_create.html', {'form': form})

# RESTAURANT SHOW
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    comments = Comment.objects.filter(restaurant=restaurant)

    env = Env()
    env.read_env()

    if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.restaurant = restaurant
                comment.created_by = request.user
                comment.save()
                return redirect('restaurant_detail', pk=pk)
    else:
        form = CommentForm(initial={'restaurant': restaurant.pk})

    context = {
        'restaurant': restaurant,
        'comments': comments,
        'form': form,
        'image_url': restaurant.image.url if restaurant.image else None,
        'MAPBOX_ACCESS_TOKEN': env('MAPBOX_ACCESS_TOKEN')
    }

    return render(request, 'restaurant_detail.html', context)

# RESTAURANT UPDATE
@login_required
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if not restaurant.user_can_delete(request.user):
        return redirect('restaurant_detail', pk=pk)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            restaurant.address = restaurant.address.replace(",", "")
            form.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)

    context = {
        'form': form,
        'restaurant': restaurant
    }
    return render(request, 'restaurant_update.html', context)

# RESTAURANT DELETE
@login_required
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if not restaurant.user_can_delete(request.user):
            return redirect('restaurant_detail', pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_index')


# COMMENT UPDATE
@login_required
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if not comment.user_can_delete(request.user):
                return redirect('restaurant_detail', pk=comment.restaurant.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=comment.restaurant.pk)
    else:
        form = CommentForm(instance=comment)

    context = {
        'comment': comment,
        'form': form
    }
    return render(request, 'comment_update.html', context)

# COMMENT DELETE
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if not comment.user_can_delete(request.user):
            return redirect('restaurant_detail', pk=comment.restaurant.pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('restaurant_detail', pk=comment.restaurant.pk)
