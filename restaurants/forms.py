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
        fields = ['body', 'margharitaindex', 'quality']
        labels = {
            'body': 'What did you think about this restaurant?',
            'margharitaindex': 'What was the price of the most basic pizza in this restaurant?',
            'quality': 'Rate the quality of your experience on a one to five scale (1 being the worst quality):',
        }
