from django.contrib import admin
from django.urls import path,include
from grid import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('face',views.face,name='face'),
    path('login',views.login,name='login'),

]

