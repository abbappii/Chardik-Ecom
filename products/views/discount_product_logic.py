
# importing
from rest_framework import generics
from products.database.discount_products import Discounts_product

from products.serializers.discount_product_serializers import (
    DiscountProductsListAPI,
    DiscountProductsSerailzers
)

'''
logic
    - list
    - retrive
'''

# list view 
class Discountproducts_list_view(generics.ListAPIView):
    queryset = Discounts_product.objects.filter(is_active=True)
    serializer_class = DiscountProductsListAPI


# single view 
class Discountproducts_Single_view(generics.RetrieveAPIView):
    queryset = Discounts_product.objects.filter(is_active=True)
    serializer_class = DiscountProductsListAPI


# create view 

class Discountproducts_Create_view(generics.CreateAPIView):
    queryset = Discounts_product.objects.filter(is_active=True)
    serializer_class = DiscountProductsSerailzers