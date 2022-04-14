from django.contrib import admin
from django.urls import path
from django.urls import URLPattern

from user_managment.views import doctors_list, home



urlpatterns=[
    path('',home),
    path('list',doctors_list),
]