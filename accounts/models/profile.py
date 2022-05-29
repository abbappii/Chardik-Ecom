'''
This file contains the followings
    - Profile models
    - Permission models 
'''

from django.db import models
from accounts.models.initials import InitModels
from accounts.models.user_model import User


# Permission Models 

class UserPermission(InitModels):
    permission_name = models.CharField(max_length=100,null=True,verbose_name=
        "Permission Name")

    def __str__(self):
        return self.permission_name

    class Meta:
        verbose_name_plural = "User Permission"

# User profile 
class Profile(InitModels):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # username=models.CharField(max_length=264, blank=True)
    full_name=models.CharField(max_length=264, blank=True,null=True)
    address=models.TextField(max_length=300, blank=True,null=True)
    city=models.CharField(max_length=40, blank=True,null=True)
    zipcode=models.CharField(max_length=10, blank=True,null=True)
    country=models.CharField(max_length=50, blank=True,null=True)
    phone=models.CharField(max_length=20, blank=True,null=True)
    customer_ID = models.CharField(max_length=20,null=True,unique=True,verbose_name=
        "Customer ID",editable=False)

    # Permission Given property
    permission = models.ManyToManyField(UserPermission,null=True)
    

    def __str__(self):
        return self.user.email 

    
    class Meta:
        verbose_name_plural = "Profile"


    # custom property
    @property
    def get_permission(self):
        permissions = [permission.permission_name for permission in self.permission.all()]
        return permissions