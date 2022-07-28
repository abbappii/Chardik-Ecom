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
o Daily sales
o Weekly sales
o Monthly sales

'''

# importing initials 

from rest_framework import generics
from django.db.models import Q


# importing models 
from products.database.init_p import   (
    Brand, Categories, Countreies
)
from products.database.products import Products

# importing API
from appFilter.serializers import (
    ProductsAPI,CategoryBaseProductsAPI, BranBasedApi, CountryBaseAPI
)

from orders.database.cart_order import Order
from rest_framework.views import APIView
from rest_framework.response import Response

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
    # lookup_field =  'slug'


# show products under Brand 

class ProductsUnderBrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BranBasedApi

## show products under Single Brand
class SingleBrandProducts(generics.RetrieveAPIView):
    queryset = Brand.objects.prefetch_related('brand')
    serializer_class = BranBasedApi
    # lookup_field =  'slug'

#show products under Country
class ProductsUnderCountryView(generics.ListAPIView):
    queryset = Countreies.objects.all()
    serializer_class = CountryBaseAPI

## show products under Single Country 
class SingleCoutryProducts(generics.RetrieveAPIView):
    queryset = Countreies.objects.prefetch_related('country')
    serializer_class = CountryBaseAPI
    # lookup_field =  'slug'



## Popular Products  List
    '''
    - Filter by start Count
    - Filter by comment count 
    '''
    
# class PopularProductsListView(generics.ListAPIView):
#     queryset = Products.objects.filter()



class Prouduct_by_review_count(generics.ListAPIView):
    serializer_class = ProductsAPI

    def get_queryset(self):
        product_by_count = Products.objects.filter(is_active=True).order_by('-review_star_count')
        return product_by_count

'''
popular product logic by
    - star count
    - comment count 

'''
class PopularProductList(generics.ListAPIView):
    # queryset = Products.objects.filter(review_star_count__gte = 4.0).
    # filter(review_comment_count={})
    serializer_class = ProductsAPI
    def get_queryset(self):
        filtered = [x for x in Products.objects.all()\
             if x.review_star_count >= 4.0 \
                  and x.review_comment_count]
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
Daily sales logic
'''
import datetime

class DailySalesOrderTimeToTimeListView(APIView):
    def get(self,request):
        queryset = Order.objects.filter(created_at=datetime.date.today(), 
        items__is_order=True
        )
        print(queryset)
        return Response(queryset)


'''
    hourly sales, 
    last 24 hours sales
    daily sales 
    weekly sales, 
    monthly sales, 
    6 monthly sales, 
    yearly sales
'''

from datetime import datetime, timedelta
from django.utils import timezone
now = timezone.now()

'''
hourly sales
'''
class HourlySales(APIView):
    
    def get(self,request):
        qs = Order.objects.filter(created_at__gte=datetime.now() - \
            timedelta(hours=1)).aggregate(total_sum=Sum('total'))
        return Response(qs)
    
'''
Daily total sales price
'''
from django.db.models import Sum
class DailyTotalSales(APIView):
    def get(self,request):
        qs = Order.objects.all().filter(created_at=now.date()).aggregate(total_sum=Sum('total'))
        return Response(qs)

# last 24 hours sales 
class Last24hoursSales(APIView):
    def get(self,request):
        qs = Order.objects.filter(created_at__gte=datetime.now() - \
            timedelta(hours=24)).aggregate(total_sum=Sum('total'))
        return Response(qs)
    

# last 7 days sales 
class WeeklySalesView(APIView):
    def get(self,request):
        qs =Order.objects.filter(created_at__gte= now - \
            timedelta(days=7)).aggregate(total_sum=Sum('total'))
        return Response(qs)
    

# last 30 days sales 
class MonthlySasleView(APIView):
    def get(self,request):
        queryset = Order.objects.filter(created_at__gte= now - \
            timedelta(days=30)).aggregate(total_sum=Sum('total'))
        return Response(queryset)

# # last 6 month sales 
month_ago = 6
class HalfYearlySalesView(APIView):
    def get(self,request):
        queryset = Order.objects.filter(created_at__gte = now - \
            timedelta(days=(month_ago * 365 / 12))).aggregate(total_sum=Sum('total'))

        return Response(queryset)

# # yearly sales =1
# class YearlySalesView(generics.ListAPIView):
#     queryset = Products.objects.filter(items__created_at__gte = now - \
#          timedelta(days=365)).aggregate(total_sum=Sum('selling_price'))
