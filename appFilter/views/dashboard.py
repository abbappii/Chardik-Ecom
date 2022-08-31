'''
Queries Related Dashboard
Transection Filter 
    - purchase by supplier
    - selling by customer 
'''

from rest_framework import generics

## importing  models 
from inventory.models import (
    Supplier
)
from accounts.models.profile import (
    Profile
)

## importing API
from appFilter.serializers import (
    Purchase_ofSupplier_API,
    Orders_of_CustomersAPI
)


## Purchase of Supplier
class Purchase_ofSupplier_View(generics.ListAPIView):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = Purchase_ofSupplier_API


## sale of Customers
class Sale_of_CustomersView(generics.ListAPIView):
    queryset = Profile.objects.filter(is_active = True)
    serializer_class = Orders_of_CustomersAPI