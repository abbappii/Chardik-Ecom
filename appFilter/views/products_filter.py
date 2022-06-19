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
from django.db.models import Q


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
    queryset = Categories.objects.all()
    serializer_class = CategoryBaseProductsAPI    

## show products under Single Category
class SingleCategoryProducts(generics.RetrieveAPIView):
    queryset = Categories.objects.prefetch_related('Category_products')
    serializer_class = CategoryBaseProductsAPI


# show products under Brand 

class ProductsUnderBrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BranBasedApi

## show products under Single Brand
class SingleBrandProducts(generics.RetrieveAPIView):
    queryset = Brand.objects.prefetch_related('brand')
    serializer_class = BranBasedApi

#show products under Country
class ProductsUnderCountryView(generics.ListAPIView):
    queryset = Countreies.objects.all()
    serializer_class = CountryBaseAPI

## show products under Single Country 
class SingleCoutryProducts(generics.RetrieveAPIView):
    queryset = Countreies.objects.prefetch_related('country')
    serializer_class = CountryBaseAPI



## Popular Products  List
    '''
    - Filter by start Count
    - Filter by comment count 
    '''
    
# class PopularProductsListView(generics.ListAPIView):
#     queryset = Products.objects.filter()









# ---abbappii
'''
popular product logic by
    - star count
    - comment count 

latest product count logic
    - by updated_at

Top sales product logic
    - order_items last 7-10 days 
    - filter by order_items quantity
'''

# popular products 
class PopularProductList(generics.ListAPIView):
    queryset = Products.objects.filter(review_star_count__gte = 4.0).filter(review_comment_count={})

# latest products 
class LatestProductList(generics.ListAPIView):
    queryset = Products.objects.all().order_by('-created_at')[:20]
    serializer_class = ProductsAPI

# Top sales product ----logic 1
class TopSalesProductsListView(generics.ListAPIView):
    queryset = Products.objects.all().order_by('-sold_count')[:20]

# Top sales products --- logic 2
import datetime
from django.db.models import Sum   
class TopSalesProductList(generics.ListAPIView):
    queryset = Products.objects.filter(orderitem=datetime.datetime.today(),
             orderitem__created_at__gt=datetime.datetime.today()
             -datetime.timedelta(days=7)).annotate(quantity_sum = 
             Sum('orderitem__quantity')).order_by('-quantity_sum')[:10]

# Price (Low to Hight , High to Low)* 
class PriceLowToHighListView(generics.ListAPIView):
    pass
