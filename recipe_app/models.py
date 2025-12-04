from django.db import models
from django import forms
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('BreakFast','BreakFast'),
    ("Lunch","Lunch"),
    ("Dinner","Dinner"),
    ("Salad","Salad"),
    ('Cold-Drinks','Cold-Drinks'),
    ('Easy','Easy'),
    
)

from django.contrib.auth.models import User


class recepie(models.Model):
  
    Title=models.CharField(max_length=30)
    Cooking_Time=models.CharField(max_length=30)
    Servings=models.CharField(max_length=30)
    Description=models.TextField(max_length=300)
    Image=models.ImageField(upload_to='images',default="")
    Ingrediants=models.CharField(max_length=300)
    Instructions=models.TextField(max_length=300)
    Category=models.CharField(choices=CATEGORY_CHOICES,max_length=50,null=True,blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    


    class Meta:
        db_table="recipe"


class recepieForm(forms.ModelForm):
    class Meta:
        model=recepie
        fields="__all__"