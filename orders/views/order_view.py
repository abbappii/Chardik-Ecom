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

        item_list = request.data

        list_item = []
        for item in item_list:


            add_item = OrderItem(
                item_id = item['item'],
                quantity = item['quantity'],
                attr = item['attr'],
                amount_item = item['amount_item'],
                total_amount_item = item['total_price'],
                is_order = True
            )
            add_item.save()

            list_item.append(add_item.id)
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