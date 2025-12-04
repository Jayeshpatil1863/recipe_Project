
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('add',v.add,name='add'),
    path('list',v.list,name='list'),
    path('search',v.search,name="search"),
    path('about',v.about,name="about"),
    path("re_search/", v.re_search, name="re_search"),  
    path("recipe/<int:id>/", v.recipe_detail, name="recipe"),
    path('edit/<int:id>/', v.recipe_edit, name="edit"),
    path('delete/<int:id>/', v.delete_recipe, name="delete"),
]

