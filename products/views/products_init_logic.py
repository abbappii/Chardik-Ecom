'''
This file contains the Business logics of the followings 

- Category (Create , Update , view , Delete)
- sub (Create , Update , view , Delete)
- brand (Create , Update , view , Delete)
- countries (Create , Update , view , Delete)
'''
from rest_framework import generics
from products.database.init_p import *
from products.serializers.init_serializers import *

class CategoriesViewSet(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

class CategoriesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class =CategoriesSerializers
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

#Sub Category part
class SubCategoriesViewSet(generics.ListCreateAPIView):
    queryset = Sub_Categories.objects.all()
    serializer_class = SubCategoriesSerializers

class SubCategoriesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_Categories.objects.all()
    serializer_class =SubCategoriesSerializers


#Brnad 
class BrandView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class =BrandSerializer

#Country part 
class CountryView(generics.ListCreateAPIView):
    queryset = Countreies.objects.all()
    serializer_class = CountriesSerializer

class CountryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countreies.objects.all()
    serializer_class =CountriesSerializer
