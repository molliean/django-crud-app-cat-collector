from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        # path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
        # cat_id is the param, so thats why we see it in kwargs
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    