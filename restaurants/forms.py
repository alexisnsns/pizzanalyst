from django import forms
from .models import Restaurant
from .models import Comment


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'body', 'cheapestslice', 'quality']
