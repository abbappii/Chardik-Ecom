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
from products.database.products import Products

# importing API
from appFilter.serializers import ProductsAPI


# products Queries show ALL

class AllProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsAPI

