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
        if self.is_valid(): #  form validation yes
            username=self.cleaned_data['username']
            password= self.cleaned_data['password']
            if not authenticate(username=username,password=password):
                raise forms.ValidationError("Invalid login")
    
class DoctorUpdateForm(forms.ModelForm):

    class Meta:
        model=Doctor
        fields= ('username','address','specialty')

    def clean_username(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            
            try:
                newform=Doctor.objects.exclude(pk=self.instance.pk).get(username=username)
            except Doctor.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use' % newform.username)

    def clean_address(self):
        if self.is_valid():
            address=self.cleaned_data['address']
            
            try:
                newform=Doctor.objects.exclude(pk=self.instance.pk).get(address=address)
            except Doctor.DoesNotExist:
                return address
            raise forms.ValidationError('address "%s" is already in use' % newform.address)
    def clean_specialty(self):
        if self.is_valid():
            specialty=self.cleaned_data['specialty']
            
            try:
                newform=Doctor.objects.exclude(pk=self.instance.pk).get(specialty=specialty)
            except Doctor.DoesNotExist:
                return specialty
            raise forms.ValidationError('Specialty "%s" is already in use' % newform.specialty)