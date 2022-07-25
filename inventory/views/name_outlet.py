
from inventory.bank_model.baccounts import Name, Outlet
from inventory.bank_serializer.name_outlet_serializers import NameSerializers, OutletSerializers

from rest_framework import generics


# name list view  
class NameListView(generics.ListAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializers

# name create view 
class NameCreateView(generics.CreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializers

# delete view 
class NameDeleteView(generics.DestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializers

# outlet create view 
class OutletCreateView(generics.CreateAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializers

# delete view 
class OutletDeleteView(generics.DestroyAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializers

# list view outlet 
class OutletListView(generics.ListAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializers
