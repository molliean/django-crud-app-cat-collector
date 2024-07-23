from django.urls import path

from . import views # import all functions in the views file and attach them to the object views

urlpatterns = [
    # django uses trailing slashes / 
    # root route will just be an empty string - localhost:8000
    # mapping a view function to a url endpoint
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    #route to create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    # class based views expect params to be named pk (primary key)
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add-feeding'),
]

