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

from rest_framework import generics


# importing models 
from products.database.init import   (
    Brand, Categories,Sub_Categories
)
from products.database.products import Products

# importing API
from appFilter.serializers import (
    ProductsAPI,CategoryBaseProductsAPI, BranBasedApi
)


# products Queries show ALL

class AllProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsAPI



# SHow products under Categories

class ProductsUnderCategoryView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoryBaseProductsAPI    



# show products under Brand 

class ProductsUnderBrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BranBasedApi