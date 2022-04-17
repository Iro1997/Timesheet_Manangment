from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        if not username:
            raise ValueError("Users must have an username")
        

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,password):
        user= self.create_user(
                
                username=username,
                password=password,
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Doctor(AbstractBaseUser):
    
    username=models.CharField(max_length=50, unique=True)
    clock_in=models.DateTimeField(auto_now=True)
    ssn=models.IntegerField(null=True)
    address=models.TextField(null=True)
    phone_number=models.CharField(max_length=10)
    office=models.TextField(null=True)
    specialty=models.CharField(max_length=30)
    file_number=models.IntegerField(null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['first_name','username']


    objects=UserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True