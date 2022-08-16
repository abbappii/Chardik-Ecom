


from datetime import datetime,timedelta
from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from orders.database.cart_order import (
    Order
)

from inventory.bank_serializer.expence_serializers import ExpenceListSerializers
from inventory.models import Purchase
from inventory.bank_model.baccounts import Expenses
from products.database.damage_products import DamageProducts


import datetime
date = datetime.date.today()
now = datetime.datetime.today()

class profit_loss_daily(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = date,
             is_active=True ).order_by('-created_at').values()
        # s1 = OrderSerializer(qs1).data

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = date).\
            order_by('created_at').values()
        # s2 = PurchaseSerialiers(qs2).data

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = date).\
            order_by('-created_at').values()
        # s3 = ExpenceListSerializers(qs3).data

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = date).\
            order_by('-created_at').values()
        # s4 = DamageProductsAPI(qs4).data

        # dict  = {
        #     's1':s1,
        #     's2':s2,
        # }
        return Response({
                
                'orders_daily':qs1,
                'Purchase_daily':qs2,
                'Expenses_daily':qs3,
                'damage_daily':qs4
                })
        # return Response(dict)


# yesterday view 
class profit_loss_yesterday(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=1),
             is_active=True ).order_by('-created_at').values()

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = now - timedelta(days=1)).\
            order_by('created_at').values()

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = now - timedelta(days=1)).\
            order_by('-created_at').values()

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = now - timedelta(days=1)).\
            order_by('-created_at').values()
        
        return Response({
                
                'orders_yesterday':qs1,
                'Purchase_yesterday':qs2,
                'Expenses_yesterday':qs3,
                'damage_yesterday':qs4
                })


# weekly profit loss report  

class profit_loss_weekly(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=7),
             is_active=True ).order_by('-created_at').values()

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = now - timedelta(days=7)).\
            order_by('created_at').values()

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = now - timedelta(days=7)).\
            order_by('-created_at').values()

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = now - timedelta(days=7)).\
            order_by('-created_at').values()
        
        return Response({
                
                'orders_weekly':qs1,
                'Purchase_weekly':qs2,
                'Expenses_weekly':qs3,
                'damage_weekly':qs4
                })


# monthly profit loss report 
class profit_loss_monthly(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=30),
             is_active=True ).order_by('-created_at').values()

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = now - timedelta(days=30)).\
            order_by('created_at').values()

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = now - timedelta(days=30)).\
            order_by('-created_at').values()

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = now - timedelta(days=30)).\
            order_by('-created_at').values()
       
        return Response({
                
                'orders_monthly':qs1,
                'Purchase_monthly':qs2,
                'Expenses_monthly':qs3,
                'damage_monthly':qs4
                })

    

# monthly profit loss report 
class profit_loss_half_yearly(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=(6 * 365 / 12)),
             is_active=True ).order_by('-created_at').values()

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = now - timedelta(days=(6 * 365 / 12))).\
            order_by('created_at').values()

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = now - timedelta(days=(6 * 365 / 12))).\
            order_by('-created_at').values()

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = now - timedelta(days=(6 * 365 / 12))).\
            order_by('-created_at').values()
      
        return Response({
                
                'orders_half_yearly':qs1,
                'Purchase_half_yearly':qs2,
                'Expenses_half_yearly':qs3,
                'damage_half_yearly':qs4
                })




# monthly profit loss report 
class profit_loss_yearly(APIView):
    def get(self,request): 
        qs1 = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=365),
             is_active=True ).order_by('-created_at').values()

        qs2 = Purchase.objects.filter(is_active=True, created_at__gte = now - timedelta(days=365)).\
            order_by('created_at').values()

        qs3 = Expenses.objects.filter(is_active=True, created_at__gte = now - timedelta(days=365)).\
            order_by('-created_at').values()

        qs4 = DamageProducts.objects.filter(is_active=True, created_at__gte = now - timedelta(days=365)).\
            order_by('-created_at').values()
        
        return Response({
                
                'orders_yearly':qs1,
                'Purchase_yearly':qs2,
                'Expenses_yearly':qs3,
                'damage_yearly':qs4
                })