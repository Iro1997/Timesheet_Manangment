#from django.views.generic import View, ListView,
from django.http import HttpResponse
from django.shortcuts import render

from user_managment.models import Doctor


def home(request):
    return HttpResponse("Still Practicing ")

def doctors_list(request):
    doctor = Doctor.objects.all()
    return render (request, 'doctors_list.html', {'key': doctor})