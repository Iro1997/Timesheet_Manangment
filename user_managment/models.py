from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    h_address=models.CharField(max_length=70,blank='False')
    o_adress=models.CharField(max_length=60,blank='True')
    phone_number=models.IntegerField(max_length=11)
    

    def __str__(self):
        return f'{self.user.id} {self.user.first_name}'


