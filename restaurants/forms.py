from django import forms
from .models import Restaurant, Comment


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'body', 'cheapestslice', 'quality']
