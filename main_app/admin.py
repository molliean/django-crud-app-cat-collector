from django.contrib import admin
from .models import Cat
# Register your models here.
admin.site.register(Cat) # creates a crud app for this model for our admins

