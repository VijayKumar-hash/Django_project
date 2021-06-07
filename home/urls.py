from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('loginuser',views.loginuser,name='loginuser'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('register',views.register, name='register'),
    path('home',views.index,name='index'),
    path('',views.index, name='index'),
]
