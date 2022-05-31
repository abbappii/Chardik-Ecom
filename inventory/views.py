from django.shortcuts import render
from inventory.models import Purchase
from inventory.serializer import PurchaseSerialiers
from rest_framework import generics


# Create your views here.
'''
Purchase show 
Purchase Edit Delete and Update class
'''

# Purchase show 
class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers



#Purchase Edit Delete and Update class
class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers