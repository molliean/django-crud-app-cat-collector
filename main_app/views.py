from django.shortcuts import render

# Create your views here.
# view functions are like controller functions
# they process http requests. in django they all go in one file


# from django.http import HttpResponse
# this is like res.send


### Friday July 19 code ONLY, for simplicity since we don't have models yet
### This is simulating objects we would retrive from the db using our model

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name 
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat("Bubbles", "Domestic Shorthair", "Loves yogurt", 12),
    Cat("Kits", "Domestic Shorthair", "Loves milk", 8),
    Cat("Lenny", "Tiger", "Loves tuna", 0),
    Cat("Mo", "Domestic Shorthair", "Loves mice", 5),
    Cat("Mika", "Maincoon", "Loves drawers", 10),
]
        

# ==============
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # 'cats' is the variable name (cat) in cats/index.html
    return render(request, 'cats/index.html', {'cats': cats})