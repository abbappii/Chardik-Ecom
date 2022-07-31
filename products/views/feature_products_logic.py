
'''
this file contains feature products logic

'''

# imort section 
from venv import create
from rest_framework import generics
from products.database.feature_product import Feature_product, Product_filter

from products.serializers.feature_products import FeatureProductSerializers, FeatureProductListSerializers

from products.serializers.feature_products import (
    ProductFilterSerializers
)
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



'''
products filiter logic 
        - list view 
        - create
        - single
        - update 
        - delete 
'''

# list view 
class ProductFilterListView(generics.ListAPIView):
    queryset = Product_filter
    serializer_class = ProductFilterSerializers

# create view 
class ProductFilterCreateView(generics.CreateAPIView):
    queryset = Product_filter
    serializer_class = ProductFilterSerializers
    
# single view 
class ProductFilterSingleView(generics.RetrieveAPIView):
    queryset = Product_filter
    serializer_class = ProductFilterSerializers
    
# update view 
class ProductFilterUpdateView(generics.UpdateAPIView):
    queryset = Product_filter
    serializer_class = ProductFilterSerializers
    
# delete view 
class ProductFilterDeleteView(generics.DestroyAPIView):
    queryset = Product_filter
    serializer_class = ProductFilterSerializers



# from rest_framework.views import APIView
# class Filter_by(APIView):

#     def get(self,request):
#         qs = Product_filter.objects.filter(product_query_select=)
