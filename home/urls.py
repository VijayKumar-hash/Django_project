from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home',views.index,name='index'),
    path('Login',views.Loginuser,name='Login'),
    path('logout',views.Logoutuser,name='Logout'),
    path('register',views.register, name='register'),
    path('',views.index, name='index')
]
