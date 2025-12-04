from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import recepie,recepieForm
from django.core.paginator import Paginator
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        user_recipes = recepie.objects.filter(user=request.user)
    else:
        user_recipes = recepie.objects.none()  
    return render(request,"home.html",{'rl':user_recipes})

from django.contrib.auth.decorators import login_required


    
def list(request):
    return render(request,"list.html",{'rl':recepie.objects.all()})

def search(request):
    if request.method=="POST":
        rTitle=request.POST.get("search")
        return render(request,"search.html",{"rl":recepie.objects.filter(Title__contains=rTitle)})
    else:
        return render(request,"search.html",{"rl":recepie.objects.all()})
    
def about(request):
    return render(request,"footer.html",{'rl':recepie.objects.all()})


def re_search(request):
    recipes = None  
    rTitle = ""

    if request.method == "POST":
        rTitle = request.POST.get("search", "").strip()
        if rTitle:
            recipes = recepie.objects.filter(Title__icontains=rTitle)
            if not recipes.exists():  
                messages.warning(request, "No results found for your search.")  # Message show hoga
                recipes = []

    return render(request, "re_search.html", {"rl": recipes, "rTitle": rTitle})




def recipe_detail(request, id):
    recipe = get_object_or_404(recepie, id=id)  
    return render(request, "recipe_detail.html", {"rl": recipe})




def home(request):
    if request.user.is_authenticated:
        user_recipes = recepie.objects.filter(user=request.user)
    else:
        user_recipes = recepie.objects.none() 
    recipes = recepie.objects.all()  
    paginator = Paginator(recipes, 8)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, 'home.html', {'page_obj': page_obj})


from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    if request.method == "POST":
        f = recepieForm(request.POST, request.FILES)
        if f.is_valid():
            recipe = f.save(commit=False)
            recipe.user = request.user 
            recipe.save()
            return redirect("/")
    else:
        f = recepieForm(initial={'user': request.user})  

    return render(request, "add_recepie.html", {"form": f})


def my_recipes(request):
    recipe_ids = request.session.get('user_recipes', [])  
    user_recipes = recepie.objects.filter(id__in=recipe_ids)  
    return render(request, "my_recipes.html", {"recipes": user_recipes})



def recipe_edit(request, id):
    recipe = get_object_or_404(recepie, id=id) 
    
    if request.method == "POST":
        form = recepieForm(request.POST, request.FILES, instance=recipe) 
        if form.is_valid():  
            form.save()
            return redirect("/")  
    else:
        form = recepieForm(instance=recipe)
    
    return render(request, "add_recepie.html", {"form": form})  


@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(recepie, id=id, user=request.user) 
    
    if request.method == "POST": 
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("/") 

    return render(request, "delete_confirm.html", {"recipe": recipe})  