'''
THis file contains the logics
    - When Blog is created 
        depending the user (admin/customer)
        the blog will be associated with them 
'''

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# importing models 
from blog.database.blog import Blog


## Differ the Blog User

@receiver(post_save,sender=Blog)
def Differ_Blog_User(sender,instance,created,*args,**kwargs):
    try:
        if created:
            if 1 in instance.user.profile.get_permission_id:
                instance.is_admin = True 
                instance.save()
            else:
                instance.is_customer = True
                instance.save()
    except Exception as e:
        print(e)