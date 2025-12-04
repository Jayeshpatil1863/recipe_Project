from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":
        f=UserCreationForm(request.POST)
        f.save()
        return redirect("/")
    else:
        return render(request,"adduser.html",{"form":UserCreationForm})
    

def login_user(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html",{"lmg":"Invalid UserName and Password"})
    else:
        return render(request,"login.html")
    
def logout_user(request):
    logout(request)
    return redirect("/")


def user_detail(request, id):  
    user = get_object_or_404(User, id=id)
    return render(request, 'add_list.html', {'user': user})



def edit(request,id):
    l = get_object_or_404(User, id=id)
    if request.method=="POST":
        u=UserCreationForm(request.POST,instance=l)
        u.save()
        return redirect("/")
    else:
        return render(request,"adduser.html",{"form":UserCreationForm(instance=l)})
    

def spe_list(request,id):
    p= get_object_or_404(User,id=id)
    if request.method=='POST':
        u=UserCreationForm(request.POST)
        u.save()
        return redirect("/")
    else:
        return render(request,"spe_addlist.html",{"form":UserCreationForm(instance=p)})
    



