'''
This file contains the logics of 
    - username Create 
    - Give Permission 
'''

from django.db.models.signals import pre_save
from django.dispatch import receiver

# importing models 
from accounts.models.user_model import User
from accounts.models.profile import Profile,UserPermission



# Creating Username 

@receiver(pre_save,sender=Profile)
def CreateUsername(sender,instance,created,*args,**kwargs):
    try:

        if created :
            user = User.objects.get(id=instance.user.id)
            user.username = f"{instance.customer_ID}_{user.email}"
            user.save()
    except Exception as e:
        print(e)


# Giver Permission to User 
@receiver(pre_save,sender=Profile)
def CreatePermission(sender,instance,created,*args,**kwargs):
    try:
        if created:
            permission_ID = UserPermission.objects.get(id=4)
            instance.permission.add(permission_ID)
            instance.save()
    except Exception as e:
        print(e)
