#from django.views.generic import View, ListView,
from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from user_managment.models import Doctor




    





def homepage(request):
    context ={}
    model=Doctor.objects.all()
    context['model']=value
    return render(request,'userspanel/index.html',context)

def aboutpage(request):
    return render(request,'about.html')

def createaccountpage(request):
    return render(request,'createaccount.html')

def loginpage(request):
    return render(request,'login.html')
