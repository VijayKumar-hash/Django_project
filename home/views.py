from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render (request,'index.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user already exists!!')
                return redirect('/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('/register')
 
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password2,email=email,username=username)
                user.save()
                return redirect('/loginuser')

        else:
            messages.error(request,'password not matching')
            return redirect('register')


    else:
        return render(request,'register.html')

def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,'Invalid credentials!!!!')
            return redirect('/loginuser')

    else:
        return render(request,'login.html')

def logoutuser(request):
    auth.logout(request)
    return redirect('/')