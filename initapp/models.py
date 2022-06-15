'''
This model database 
    - contact Us
'''

from django.db import models
from accounts.models.initials import InitModels


class ContactUs(InitModels):
    personName = models.CharField(max_length=300,null=True,verbose_name="Person Name")
    subject = models.CharField(max_length=400,null=True,verbose_name="Subject")
    c_message  = models.TextField(null=True,blank=True)
    email = models.CharField(max_length=300,null=True,verbose_name="Email")

    def __str__(self):
        return str(self.subject)

    
    class Meta:
        verbose_name_plural = "Contact Us"
        

