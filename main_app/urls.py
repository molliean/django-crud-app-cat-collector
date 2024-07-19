from django.urls import path

from . import views # import all functions in the views file and attach them to the object views

urlpatterns = [
    # django uses trailing slashes / 
    # root route will just be an empty string - localhost:8000
    # mapping a view function to a url endpoint
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
]

