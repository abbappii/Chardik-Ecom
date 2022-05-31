

'''
This file contains of 
    - Supplier View functions ( CRUD )
'''


# import section 

from rest_framework import generics
from inventory.models import Supplier
from inventory.serializer import SupplierSerializers

'''
Supplier views
        - ListView
        - Single view
        - Create view
        - Delete view
        - Update view 
'''

# view List Function 
class SupplierListView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


# Single View 
class SupplierRetrieveView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

#  Create View 
class SupplierCreateApiView(generics.CreateAPIView):
    queryset = Supplier
    serializer_class = SupplierSerializers

# delete View 
class SupplierDeleteApiView(generics.DestroyAPIView):
    queryset = Supplier
    serializer_class = SupplierSerializers


# Supplier Edit View 
class SupplierEditApiView(generics.UpdateAPIView):
    queryset = Supplier
    serializer_class = SupplierSerializers