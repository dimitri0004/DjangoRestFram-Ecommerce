from django.contrib import admin
from django.urls import path
from .views import index,first_api

urlpatterns = [
    path('',index,name="index"),
    path('index',first_api,name="first_api"),

]