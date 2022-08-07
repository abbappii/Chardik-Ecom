
from inventory.models import Purchase
from inventory.serializer import (
    PurchaseSerialiers, 
    PurchaseCreateSerializers,
    SupplierDueReportsAPI
    )
from rest_framework import generics


# Create your views here.
'''
Purchase show 
Purchase Edit Delete and Update class
'''

# view List Function 

class PurchaseView(generics.ListAPIView):
    queryset = Purchase.objects.all().order_by('-updated_at')
    serializer_class = PurchaseSerialiers


# Single View 

class PurchaseSingleView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers


#  Create View 

class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializers


# delete View 

class PurchaseDeleteView(generics.DestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers


# Single Edit View 

class PurchaseEditView(generics.UpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializers



#### Due supplier view 
class SupplierDue_ReportsView(generics.ListAPIView):
    queryset = Purchase.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = SupplierDueReportsAPI

# supplier due delte view 
class SupplierDue_ReportsDeleteView(generics.DestroyAPIView):
    queryset = Purchase.objects.filter(is_active=True)
    serializer_class = SupplierDueReportsAPI