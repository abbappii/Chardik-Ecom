
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,PermissionsMixin, BaseUserManager
    )
from django.utils.translation import gettext_lazy as _

'''
MyUserManager
User
Profile
'''

#Create user and super user

class MyUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User given email and password"""
        if not email:
            raise ValueError(_("The Email is must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Supperuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)


# over write AbstractBaseUser and set email 
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=300,unique=True,null=True,
        verbose_name="Username")
    email=models.CharField(max_length=200,blank=True,null=True)
    is_staff=models.BooleanField(_('staff status'),
    default=False,
     help_text=_('Designates whether the user can log in this site'))

    is_active=models.BooleanField(_('active'),default=True,
     help_text=_('Designates whether this user should be treated as active .\
      Unselected this instead of deleting accounts'))

    password = models.CharField(max_length=1500,null=True)
    confirm_password = models.CharField(max_length=1500,null=True)
    date_joined=models.DateField(auto_now_add=True)

    # username=models.CharField(max_length=264, blank=True)
    # full_name=models.CharField(max_length=264, blank=True)
    # address=models.TextField(max_length=300, blank=True)
    # city=models.CharField(max_length=40, blank=True)
    # zipcode=models.CharField(max_length=10, blank=True)
    # country=models.CharField(max_length=50, blank=True)
    # phone=models.CharField(max_length=20, blank=True)
    




    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']
    objects=MyUserManager()

    def __str__(self):
        return str(self.username)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    class Meta:
        app_label = 'accounts'


