from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('login_page',views.login_page, name='login_page'),
    path('register',views.register_page, name='register'),
    path('home',views.home, name='home'),
    path('signup',views.Signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    
]
