
'''
this file contains feature products logic

'''

# imort section 
from venv import create
from rest_framework import generics
from products.database.feature_product import BannerProduct, Banner

from products.serializers.feature_products import BannerProductSerializers, BannerProductListSerializers

from products.serializers.feature_products import (
    BannerSerializers
)
'''
feature products logic 
        - list view 
        - create
        - update 
        - delete 
'''

# feature product list view 
class BannerProductListView(generics.ListAPIView):
    queryset = BannerProduct.objects.all()
    serializer_class = BannerProductListSerializers

# create view 
class BannerProductCreateView(generics.CreateAPIView):
    queryset = BannerProduct.objects.all()
    serializer_class = BannerProductSerializers

# update/edit view 
class BannerProductUpdateView(generics.UpdateAPIView):
    queryset = BannerProduct.objects.all()
    serializer_class = BannerProductSerializers

# delete view 
class BannerProductDeleteView(generics.DestroyAPIView):
    queryset = BannerProduct.objects.all()
    serializer_class = BannerProductSerializers



'''
products filiter logic 
        - list view 
        - create
        - single
        - update 
        - delete 
'''

# list view 
class BannerListView(generics.ListAPIView):
    queryset = Banner
    serializer_class = BannerSerializers

# create view 
class BannerCreateView(generics.CreateAPIView):
    queryset = Banner
    serializer_class = BannerSerializers
    
# single view 
class BannerSingleView(generics.RetrieveAPIView):
    queryset = Banner
    serializer_class = BannerSerializers
    
# update view 
class BannerUpdateView(generics.UpdateAPIView):
    queryset = Banner
    serializer_class = BannerSerializers
    
# delete view 
class BannerDeleteView(generics.DestroyAPIView):
    queryset = Banner
    serializer_class = BannerSerializers



# from rest_framework.views import APIView
# class Filter_by(APIView):

#     def get(self,request):
#         qs = Product_filter.objects.filter(product_query_select=)
