


from datetime import datetime,timedelta
from re import S
from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from orders.database.cart_order import (
    Order
)
from orders.serializers import (
    OrderSerializer,
)
from inventory.bank_serializer.expence_serializers import ExpenceListSerializers
from inventory.serializer import (
    PurchaseSerialiers
)
from inventory.models import Purchase
from inventory.bank_model.baccounts import Expenses
from products.database.damage_products import DamageProducts

from products.serializers.damage_pro_serializers import (
    DamageProductsAPI
)

import datetime
date = datetime.date.today()
now = datetime.datetime.today()

class profit_loss_daily(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = date, is_active=True ).order_by('-created_at')
        s1 = OrderSerializer(qs1).data

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = date).order_by('created_at')
        s2 = PurchaseSerialiers(qs2).data

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = date).order_by('-created_at')
        s3 = ExpenceListSerializers(qs3).data

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = date).order_by('-created_at')
        s4 = DamageProductsAPI(qs4).data

        # dict  = {
        #     's1':s1,
        #     's2':s2,
        # }
        return Response({
                's1':s1,
                })
        # return Response(dict)

