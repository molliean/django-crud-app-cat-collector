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
    
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default=MEALS[0][0]
        # if we wanted lunch to be the default it wo0uld be [1][0] or dinner it would be [2][0]
    )

    # create a cat_id column on the Feeding table in the database
	# (it automatically appends, _id, you don't put that. Just lowercase modelname of related model)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    