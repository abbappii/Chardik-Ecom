'''
This file contains the 
    - order management 
    - cart management
'''

from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# importing permission 
from MainApplication.scripts.permission import ( 
    IsAdmin, 
    IsCustomer, 
    IsManager, 
    IsStuff
)
# importing models 
from orders.database.cart_order import (
    Order,
    OrderItem
)
from products.database.products import (
    Products
)
# importing serializers
from orders.serializers import (
    OrderAPI,
    OrderSerializer
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
            get_product = Products.objects.get(id=add_item.item_id)
            # print(get_product)
            get_product.stock_count += int(item['quantity'])
            get_product.save()

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
                apifetch.data,
                # {'success':'Order is Updated'},
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




# order list view 
class OrderListview(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

# order updateview
class OrderUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdmin]
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderAPI

#order customer view

class UserOrderListView(generics.ListAPIView):
    permission_classes = [IsCustomer]
    queryset = Order.objects.filter(is_active=True) 
    serializer_class = OrderSerializer

    def get(self,request):
        customer = request.user.profile
        query = Order.objects.filter(customer=customer,is_active=True)
        serializer = OrderSerializer(query, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)

#order single view
class OrderSingleView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()  
          