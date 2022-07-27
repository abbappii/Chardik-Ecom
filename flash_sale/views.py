'''
This file contains the Logics 
    - Flash Sale 
    - Flash Products 
'''

# importing Initials 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView
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

## Flash sale Inactive functions

class FlashSale_OFF(GenericAPIView):

    def get(self,request,flashID):
        get_flash_obj = FlashSale.objects.filter(id=flashID)
        if get_flash_obj:

            for product in get_flash_obj.products.all():
                product.is_active = False
                product.save()
            return Response({
                'Success':'Flash Sale Obj is Closed'
            },status=status.HTTP_202_ACCEPTED)

        else:
            return Response({
                'Error':'Flash Sale Obj ID didnt match'
            },status=status.HTTP_404_NOT_FOUND)


'''
Flash Products View Logics
    - create 
    - View 
    - update 
    - delete 
'''

## Create View 
class FlashProducts_createView (GenericAPIView):
    queryset = FlashProducts.objects.filter(is_active = True)
    serializer_class = FlashSale_ProductAPI

    def post(self,request):
        apifetch = FlashSale_ProductAPI(data=request.data)

        if apifetch.is_valid():
            obj_check = FlashProducts.objects.\
                    filter(flash_sale = apifetch.validated_data['flash_sale'],
                    flash_product=apifetch.validated_data['flash_product'])
            if obj_check:
                return Response({
                    'Error':'Flash Obj Already Exits !'
                },status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                apifetch.save()
                return Response({
                    'Success':'Flash Obj Created'
                },status=status.HTTP_201_CREATED)
        else:
            return Response(apifetch.errors)





    

