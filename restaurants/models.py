from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name

    def average_quality(self):
        return self.comments.aggregate(avg_quality=Avg('quality'))['avg_quality']

class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=20)
    body = models.TextField()
    cheapestslice = models.FloatField(default=0, validators=[MinValueValidator(0)])
    quality = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
