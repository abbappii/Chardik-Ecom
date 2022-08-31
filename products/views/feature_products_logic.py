
# '''
# this file contains feature products logic

# '''

# # imort section 
from rest_framework import generics
from products.database.feature_product import (
    BannerProduct, 
    Banner
)

from products.serializers.feature_products import ( 
    Banner_API, 
    Banner_API_func,
    Banner_Product_API, 
    BannerProduct_API_show
)


# '''
# Banner view logics 
#         - list view 
#         - create
#         - update 
#         - delete 
# '''

# # banner product list view 

class Banner_createView(generics.CreateAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = Banner_API_func

# list view 
class Banner_ListView(generics.ListAPIView):
    queryset = Banner.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = Banner_API

# single view 
class Banner_SingleView(generics.RetrieveAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = Banner_API

# update, delete view 
class Banner_update_deleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = Banner_API_func

'''
Banner products view logics
    - create
    - list
    - update
    - delete

'''
from rest_framework.response import Response
from rest_framework import status

# create view 
class BannerProducts_createView(generics.GenericAPIView):
    queryset = BannerProduct.objects.filter(is_active=True)
    serializer_class = Banner_Product_API

    def post(self,request):
        data = request.data
        serializer = Banner_Product_API(data=data)

        if serializer.is_valid():
            obj_check = BannerProduct.objects.filter(
                            banner=serializer.validated_data['banner'],
                            banner_product=serializer.validated_data['banner_product']
            )
            if obj_check:
                return Response({
                    'Error':'Banner Obj Already Exits !'
                },status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                serializer.save()
                return Response({
                    'Success':'Banner Obj Created'
                },status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    
# Banner products single view 
class BannerProducts_SingleView(generics.RetrieveAPIView):
    queryset = BannerProduct.objects.filter(is_active=True)
    serializer_class = BannerProduct_API_show


# Banner Products delete 
class BannerProducts_DeleteView(generics.DestroyAPIView):
    queryset = BannerProduct.objects.filter(is_active=True)
    serializer_class = Banner_Product_API

class BannerListView(generics.ListAPIView):
    queryset = BannerProduct.objects.filter(is_active=True)
    serializer_class = Banner_Product_API
    
