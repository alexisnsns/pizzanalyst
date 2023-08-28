from django import forms
from .models import Restaurant, Comment


class RestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.initial['name'] = self.instance.name
            self.initial['description'] = self.instance.description
            self.initial['address'] = self.instance.address


    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'cheapestslice', 'quality']
