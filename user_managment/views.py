#from django.views.generic import View, ListView,
from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate, logout
from user_managment.forms import DoctorAuthenticationForm, DoctorUpdateForm, RegistrationForm
from user_managment.models import Doctor




def registration_view(request):
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            account=form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(username=username,password=raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registration_form']=form
    else:
        form= RegistrationForm()
        context['registration_form']=form
    return render(request, 'userspanel/register.html',context)



def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context ={}
    user=request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form= DoctorAuthenticationForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)

            if user:
                login(request,user)
                return redirect('home')
    else:
        form=DoctorAuthenticationForm()
    context['login_form']=form
    return render(request, 'userspanel/login.html',context) 


def update_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}

    if request.POST:
        form=DoctorUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form=DoctorUpdateForm(
            initial={
                'username': request.user.username,
                'password':request.user.password
            }
        )
    context['update_form']= form
    return render(request,'userspanel/doctorupdate.html',context)

        







def homepage(request):
    context ={}
    model=Doctor.objects.all()
    context['model']=model
    return render(request,'userspanel/navbar.html',context)

def aboutpage(request):
    return render(request,'about.html')

def createaccountpage(request):
    return render(request,'createaccount.html')

def loginpage(request):
    return render(request,'login.html')
