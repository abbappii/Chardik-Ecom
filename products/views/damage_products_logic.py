

'''
This file contains 
    - add damage products
    - Damage proucts
        --logics
'''

# importing from rest framework section  
from pydoc import getpager
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