from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login,authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render (request,'index.html')

def register(request):
    form = UserCreationForm()
    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('Login')

    context = {'form':form}
    return render(request,'register.html',context)


def Loginuser(request):
    if request.method=='POST':
        user = request.POST.get('user')
        pwd = request.POST.get('password')
        user = authenticate(user=user,password=pwd)

        if user is None:
            login(request,user)
        else:
            pass

    return render(request,'Login.html')

def Logoutuser(request):
    logout(request)
    return redirect("/Login.html")
