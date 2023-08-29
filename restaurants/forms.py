from django import forms
from .models import Restaurant, Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'image']
        labels = {
            'name': 'What is the name of the restaurant?',
            'description': 'How would you describe this restaurant?',
            'address': 'What is the address of the restaurant?',
            'image': 'You can add a picture:'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'cheapestslice', 'quality']
        labels = {
            'body': 'Share your thoughts:',
            'cheapestslice': 'Rate the affordability one a one to five scale:',
            'quality': 'Rate the quality on a one to five scale:',
        }
