from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from user_managment.models import Doctor

class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=30,help_text="Required, Add a valid username")

    class Meta:
        model=Doctor
        fields=("username",'password1','password2')

class DoctorAuthenticationForm(forms.ModelForm):

    password=forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model=Doctor
        fields =('username','password')
    
    def clean(self):
        username=self.cleaned_data['username']
        password= self.cleaned_data['password']
        if not authenticate(username=username,password=password):
            raise forms.ValidationError("Invalid login")