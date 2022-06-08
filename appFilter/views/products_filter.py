'''
Queries related to products goes in this file 

Frontend
○ Products * 
○ Category Based products*
○ Brand Based Products*
○ Country Based Products*
○ Popular products* 
○ Latest Products*
○ Top Sales Products*
○ Price (Low to Hight , High to Low)*
○ Flash deal Based Product*
'''

# importing initials 

from typing import Counter
from rest_framework import generics


# importing models 
from products.database.init import   (
    Brand, Categories, Countreies,Sub_Categories
)
from products.database.products import Products

# importing API
from appFilter.serializers import (
    ProductsAPI,CategoryBaseProductsAPI, BranBasedApi, CountryBaseAPI
)


# products Queries show ALL

class AllProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsAPI



# SHow products under Categories

class ProductsUnderCategoryView(generics.ListAPIView):
    queryset = Categories.objects.prefetch_related('Category_products')
    serializer_class = CategoryBaseProductsAPI    

## show products under Single Category
class SingleCategoryProducts(generics.RetrieveAPIView):
    queryset = Categories.objects.prefetch_related('Category_products')
    serializer_class = CategoryBaseProductsAPI


# show products under Brand 

class ProductsUnderBrandView(generics.ListAPIView):
    queryset = Brand.objects.prefetch_related('brand')
    serializer_class = BranBasedApi

## show products under Single Brand
class SingleBrandProducts(generics.RetrieveAPIView):
    queryset = Brand.objects.prefetch_related('brand')
    serializer_class = BranBasedApi

#show products under Country
class ProductsUnderCountryView(generics.ListAPIView):
    queryset = Countreies.objects.prefetch_related('country')
    serializer_class = CountryBaseAPI

## show products under Single Country 
class SingleCoutryProducts(generics.RetrieveAPIView):
    queryset = Countreies.objects.prefetch_related('country')
    serializer_class = CountryBaseAPI
    