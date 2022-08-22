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

from accounts.models.profile import Profile

# importing serializers
from orders.serializers import (
    OrderAPI,
    OrderSerializer,
    CustomerOrdersViewAdminSerializer,
)
from rest_framework.decorators import permission_classes
from MainApplication.scripts.phone_SMS_settings import SMS_for_Phone_Message

import datetime
tday = datetime.date.today()

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
            get_product.sold_count += int(item['quantity'])
            # print("sold count:",get_product.sold_count)
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
        # phone = request.data.get('mobile')
        # print(phone)
        apifetch = OrderAPI(add_user,data=request.data)
        if apifetch.is_valid():
            apifetch.save()

            phone = apifetch.validated_data['mobile']
            message = f"You have successfully created order at Chardike.com"
            SMS_for_Phone_Message(phone,message).start()

            return Response(
                apifetch.data,
                # {'success':'Order is Updated'},
                status=status.HTTP_201_CREATED)
        else:
            return Response(apifetch.errors)


# order list view 
class OrderListview(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

# order updateview
@permission_classes([IsAdmin|IsManager|IsStuff])
class OrderUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdmin|IsManager|IsStuff]
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
          


# admin view of custommer orders 
class orderviewofcustomerAdminview(generics.ListAPIView):
    queryset = Order.objects.filter(is_active=True).order_by('-created_at') 
    serializer_class = CustomerOrdersViewAdminSerializer
    permission_classes = [IsAdmin]

    def get(self,request,profileID):
        customer = Profile.objects.get(id = profileID)
        query = Order.objects.filter( customer = customer, is_active=True)
        serializer = CustomerOrdersViewAdminSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# today orders list \

class todays_OrderList(generics.ListAPIView):
    queryset = Order.objects.filter(created_at__gte = tday).order_by('-created_at')
    serializer_class = OrderSerializer