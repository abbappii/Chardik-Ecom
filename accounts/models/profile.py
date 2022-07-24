'''
This file contains the followings
    - Profile models
    - Permission models 
'''

from django.db import models
from django.db.models.signals import pre_save
from accounts.models.initials import InitModels
from accounts.models.user_model import User
from MainApplication.scripts.customer_ID import unique_customerID_generate


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', 
        null=True)
    # username=models.CharField(max_length=264, blank=True)
    full_name=models.CharField(max_length=264, blank=True,null=True)

    dob = models.DateField(max_length=8,null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True) 
    bio = models.TextField(null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_image', blank=True) 

    address=models.TextField(max_length=300, blank=True,null=True)
    city=models.CharField(max_length=40, blank=True,null=True)
    zipcode=models.CharField(max_length=10, blank=True,null=True)
    country=models.CharField(max_length=50, blank=True,null=True)

    phone=models.CharField(max_length=20, blank=True,null=True,unique=True)
    is_phone_verified = models.BooleanField(default=False)
    phone_otp = models.CharField(max_length=7,null=True,blank=True)
    customer_ID = models.CharField(max_length=20,null=True,unique=True,verbose_name=
        "Customer ID",editable=False)

    # Permission Given property
    permission = models.ManyToManyField(UserPermission)
    
    points_gained = models.IntegerField(default=0)


    def __str__(self):
        return self.full_name

    

    class Meta:
        verbose_name_plural = "Profiles"

    # custom property
    @property
    def get_permission(self):
        permissions = [permission.permission_name for permission in self.permission.all()]
        return permissions

    @property
    def get_permission_id(self):
        permissions = [permission.id for permission in self.permission.all()]
        return permissions

    # unique customer ID creating process
def make_customer_ID(sender,instance,*args,**kwargs):
    if not instance.customer_ID:
        instance.customer_ID =unique_customerID_generate(instance)

pre_save.connect(make_customer_ID,sender=Profile)




## Billing Address Models 

class BillingAddress(InitModels):
    customer = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,
        null=True,verbose_name="Customer Name")
    '''
    name
    phone 
    email
    '''
    name = models.CharField(max_length=255,null=True, blank=True)
    email = models.CharField(max_length=255, null=True,blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    region = models.CharField(max_length=300,null=True,
        verbose_name="Region Name")
    city = models.CharField(max_length=300,null=True,
        verbose_name="City Name")
    area = models.CharField(max_length=500,null=True,
        verbose_name="Area Name",blank=True)
    post_code = models.CharField(max_length=100,null=True,
        verbose_name="Post Code",blank=True)
    address = models.TextField(null=True,verbose_name="Address")
    # By default this model will save as a shipping address 
    # But when Is_billing = True , it will save as a billing address
    is_billing =models.BooleanField(default=False,verbose_name="Is Billing Address")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name_plural = "Shipping Address"
        


