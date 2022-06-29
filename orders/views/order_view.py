'''
This file contains the 
    - order management 
    - cart management
'''
import json
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from products.database.products import Products
from django.http import JsonResponse

# importing models 
from orders.database.cart_order import (
    Order,
    OrderItem
)
from orders.serializers import (
    OrderAPI
)

## Order Item added 

class AddOrderItem(GenericAPIView):
    
    def post(self,request):
        # data = request.data
        # item_list = dict((request.data).lists())['id','quantity','attr','amount_item']
        item_list = request.data
        print(item_list.json())
        list_item = []
        for item in item_list:
            print (item)
        #     # item_id = Products.objects.filter(id=item['id']).first()
        #     # print(item_id)
            # add_item = OrderItem(
            #     # item = item['id'],
            #     # item = Products.objects.filter(id=item['id']).first(),
            #     quantity = item['quantity'],
            #     # attr = item['attr'],
            #     # amount_item = item['amount'],
            #     is_order = True
            # )
            # add_item.save()
            # list_item.append(add_item)
        return Response (list_item)


## Order Add
class OrderView(GenericAPIView):
    serializer_class = OrderAPI
    queryset = Order.objects.filter(is_active=True)

    def post(self,request):
        user = request.user.profile
        add_user = Order(customer=user)
        apifetch = OrderAPI(add_user,data=request.data)
        if apifetch.is_valid():
            apifetch.save()
            return Response(
                {'success':'Order is Updated'},
                status=status.HTTP_201_CREATED)
        else:
            return Response(apifetch.errors)


'''

{
    {
        "id":"1",
        "quantity":"3"
    },
    {
        "id":"2",
        "quantity":"3"
    }
}
'''