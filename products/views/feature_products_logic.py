
'''
this file contains feature products logic

'''

# imort section 
from venv import create
from rest_framework import generics
from products.database.feature_product import Feature_product

from products.serializers.feature_products import FeatureProductSerializers, FeatureProductListSerializers

'''
feature products logic 
        - list view 
        - create
        - update 
        - delete 
'''

# feature product list view 
class FeatureProductListView(generics.ListAPIView):
    queryset = Feature_product.objects.all()
    serializer_class = FeatureProductListSerializers

# create view 
class FeatureProductCreateView(generics.CreateAPIView):
    queryset = Feature_product.objects.all()
    serializer_class = FeatureProductSerializers

# update/edit view 
class FeatureProductUpdateView(generics.UpdateAPIView):
    queryset = Feature_product.objects.all()
    serializer_class = FeatureProductSerializers

# delete view 
class FeatureProductDeleteView(generics.DestroyAPIView):
    queryset = Feature_product.objects.all()
    serializer_class = FeatureProductSerializers

