

'''
This file contains 
    - add damage products
    - Damage proucts
        --logics
'''

# importing from rest framework section  
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# importing models 
from products.database.damage_products import (
    DamageProducts,AddDamageProduct
)

from products.database.products import (
    Products
)

from products.serializers.damage_pro_serializers import (
    DamageProductsAPI,
    DamageProductsSerializers
)

class AddDamageProductsView(GenericAPIView):
    
    def post(self,request):

        damage_product_list = request.data
        list_products_item = []

        for product in damage_product_list:
            add_item = AddDamageProduct(
                product_id = product['product'],
                quantity = product['quantity'],
                loss_per_unit = product['loss_per_unit']
            )
            add_item.save()
            # get product 
            get_products = Products.objects.get(id=add_item.product_id)
            print(get_products)
            get_products.stock_count += int(product['quantity'])
            get_products.save()

            list_products_item.append(add_item.id)
        return Response(list_products_item)
    

# damage product create logic 

class DamageProductsView(GenericAPIView):
    queryset = DamageProducts.objects.all()
    serializer_class = DamageProductsSerializers

    def post(self,request):

        data = request.data
        serializer = DamageProductsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(serializer.errors)  
        
# damage products list view 
class DamageProductsListView(generics.ListAPIView):
    queryset = DamageProducts.objects.all()
    serializer_class = DamageProductsAPI 

# update view 
class DamageProductsUpdateView(generics.UpdateAPIView):
    queryset = DamageProducts.objects.all()
    serializer_class = DamageProductsSerializers

# delete view 
class DamageProductsDeleteeView(generics.DestroyAPIView):
    queryset = DamageProducts.objects.all()
    serializer_class = DamageProductsSerializers

# delete view 
class DamageProductsSingleView(generics.RetrieveAPIView):
    queryset = DamageProducts.objects.all()
    serializer_class = DamageProductsAPI


