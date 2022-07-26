'''
This file contains the Logics 
    - Flash Sale 
    - Flash Products 
'''

# importing Initials 
from rest_framework import generics
from rest_framework.decorators import permission_classes

## importing models 
from flash_sale.models import(
    FlashSale,
    FlashProducts
)

## importing APIs
from flash_sale.serializers import (
    FlashSale_API,
    FlashSale_ProductAPI,
    FlashSale_API_func
)


'''
Flash Sale View Logics 
    - create 
    - View 
    - update 
    - delete 
'''

## Create View 
class FlashSale_createView (generics.CreateAPIView):
    queryset = FlashSale.objects.filter(is_active = True)
    serializer_class = FlashSale_API_func

## List View 
class FlashSale_listView (generics.ListAPIView):
    queryset = FlashSale.objects.filter(is_active = True)
    serializer_class = FlashSale_API

## Single View 
class FlashSale_singleView(generics.RetrieveAPIView):
    queryset = FlashSale.objects.filter(is_active = True)
    serializer_class = FlashSale_API

## Update , Delete view 
class FlashSale_update_deleteView (generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashSale.objects.filter(is_active = True)
    serializer_class = FlashSale_API_func



'''
Flash Products View Logics
    - create 
    - View 
    - update 
    - delete 
'''

## Create View 
class FlashProducts_createView (generics.CreateAPIView):
    queryset = FlashProducts.objects.filter(is_active = True)
    serializer_class = FlashSale_ProductAPI

