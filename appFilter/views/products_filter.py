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






'''
popular product logic by
    - star count
    - comment count 

'''
class PopularProductList(generics.ListAPIView):
    # queryset = Products.objects.filter(review_star_count__gte = 4.0).filter(review_comment_count={})
    serializer_class = ProductsAPI
    def get_queryset(self):
        filtered = [x for x in Products.objects.all() if x.review_star_count >= 4.0 and x.review_comment_count]
        print(filtered)
        return filtered


'''
latest product count logic
    - by created_at
'''
class LatestProductList(generics.ListAPIView):
    queryset = Products.objects.all().order_by('-created_at')[:20]
    serializer_class = ProductsAPI



'''
Top sales product logic
    - using sold_count field
'''
class TopSalesProductsListView(generics.ListAPIView):
    queryset = Products.objects.all().order_by('-sold_count')[:20]
    serializer_class = ProductsAPI


'''
Product low to high 
    - ordering by price

'''

