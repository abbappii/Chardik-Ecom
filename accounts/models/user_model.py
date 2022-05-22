from accounts.models.initials import InitModels
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
 PermissionsMixin, BaseUserManager)
from django.utils.translation import gettext_lazy

'''
MyUserManager
User
Profile
'''

#Create user and super user

class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None,confirm_password=None, **extra_fields):
        if not email:
            raise ValueError("Must Have to Eamil")
        email = self.normalize_email(email)
        user =self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuse must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuse must have is_superuser=True')
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuse must have is_active=True')

        return self.create_user(email,password, **extra_fields)


# over write AbstractBaseUser and set email 
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True, null=False)
    is_staff=models.BooleanField(gettext_lazy('staff status'),
    default=False,
     help_text=gettext_lazy('Designates whether the user can log in this site'))

    is_active=models.BooleanField(gettext_lazy('active'),default=True,
     help_text=gettext_lazy('Designates whether this user should be treated as active .\
      Unselected this instead of deleting accounts'))
    date_joined=models.DateField(auto_now_add=True)

    # username=models.CharField(max_length=264, blank=True)
    # full_name=models.CharField(max_length=264, blank=True)
    # address=models.TextField(max_length=300, blank=True)
    # city=models.CharField(max_length=40, blank=True)
    # zipcode=models.CharField(max_length=10, blank=True)
    # country=models.CharField(max_length=50, blank=True)
    # phone=models.CharField(max_length=20, blank=True)
    


    USERNAME_FIELD='email'
    objects=MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    class Meta:
        app_label = 'accounts'


# User profile 
class Profile(InitModels):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    username=models.CharField(max_length=264, blank=True)
    full_name=models.CharField(max_length=264, blank=True)
    address=models.TextField(max_length=300, blank=True)
    city=models.CharField(max_length=40, blank=True)
    zipcode=models.CharField(max_length=10, blank=True)
    country=models.CharField(max_length=50, blank=True)
    phone=models.CharField(max_length=20, blank=True)
    

    def __str__(self):
        return self.user.email 