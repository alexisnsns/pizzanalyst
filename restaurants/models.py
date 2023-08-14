from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)

    def __str__(self):
        return self.name

    def average_quality(self):
        return self.comments.aggregate(avg_quality=Avg('quality'))['avg_quality']

    class Meta:
        permissions = [('can_delete_restaurant', 'Can delete restaurant')]

    def user_can_delete(self, user):
        return user == self.created_by

class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    cheapestslice = models.FloatField(default=0, validators=[MinValueValidator(0)])
    quality = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)

    def __str__(self):
        return self.body

    class Meta:
        permissions = [('can_delete_comment', 'Can delete comment')]

    def user_can_delete(self, user):
        return user == self.created_by
