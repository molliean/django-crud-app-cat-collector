from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Cat
from .forms import FeedingForm
# from django.http import HttpResponse
# this is like res.send

# <model_name>_form.html. the model = Cat get used in the cat_form.html as cat.name, cat.breed, etc.

class CatCreate(CreateView):
    model = Cat 
    fields = '__all__' # this references the model fields
    # this is how to define a redirect, but we are using the get_absolute_url on the model
    # success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat 
    #disallow updating of cat's name
    fields=['breed', 'description', 'age']
    # this is how to define a redirect, but we are using the get_absolute_url on the model
    # success_url = '/cats/'

class CatDelete(DeleteView):
    model = Cat 
    # need to use success route here.
    success_url = '/cats/'

# view functions are like controller functions
# they process http requests. in django they all go in one file
# ===================================================================

### Friday July 19 code ONLY, for simplicity since we don't have models yet
### This is simulating objects we would retrive from the db using our model

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name 
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat("Bubbles", "Domestic Shorthair", "Loves yogurt", 12),
#     Cat("Kits", "Domestic Shorthair", "Loves milk", 8),
#     Cat("Lenny", "Tiger", "Loves tuna", 0),
#     Cat("Mo", "Domestic Shorthair", "Loves mice", 5),
#     Cat("Mika", "Maincoon", "Loves drawers", 10),
# ]
        

# ==============
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # 'cats' is the variable name (cat) in cats/index.html
    cats = Cat.objects.all() # using our model to select all rows in the cats table
    return render(request, 'cats/index.html', {'cats': cats})

# cat_id comes from the param name in the urls.py. i.e. 
# path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
# these have to match
def cat_detail(request, cat_id):
    # user our model to find a cat in the row that matches cat_id
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm() # this creates a form from our class
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

def add_feeding(request, cat_id): #cat_id comes from the param name in urls.py
    # create a ModelForm instance ie filling out the form using the data in request.POST.
    form = FeedingForm(request.POST) #request.POST is like req.body
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        #create an object to be saved to the db
        new_feeding = form.save(commit=False)
        # add the cat_id to the object that is going to be added as a new row in the feeding table in psql
        new_feeding.cat_id = cat_id
        new_feeding.save() # enters a new row in feeding table in psql
    return redirect('cat-detail', cat_id=cat_id)
    # cat_id is the param in on the url for cat-detail
    # the value is the param in the argument in the add_feeding function