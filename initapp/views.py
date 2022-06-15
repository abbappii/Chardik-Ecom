
'''
    This file contains contactus 
    -createView logic
'''

# import section 

from rest_framework import generics

from .models import ContactUs
from .serializers import ContactUsSerializers


class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs
    serializer_class = ContactUsSerializers