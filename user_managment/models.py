from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username, first_name, password=None):
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have an first name")

        user = self.model(
            first_name=first_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,first_name,password):
        user= self.create_user(
                first_name=first_name,
                username=username,
                password=password,
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Doctor(AbstractBaseUser):
    first_name=models.CharField(max_length=40)
    username=models.CharField(max_length=50, unique=True)
    clock_in=models.DateTimeField(auto_now=True)
    ssn=models.IntegerField()
    address=models.TextField()
    phone_number=models.IntegerField()
    office=models.TextField()
    specialty=models.CharField(max_length=30)
    file_number=models.IntegerField()
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['first_name','username']


    object=UserManager()

    def __str__(self):
        return self.first_name +','+ self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True