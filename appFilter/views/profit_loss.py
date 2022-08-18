


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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
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
                
                'orders':qs1,
                'Purchase':qs2,
                'Expenses':qs3,
                'damage':qs4
                })



# present profit loss report 
class profit_loss_daily_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = date).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte = date).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte = date).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte = date).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })




class profit_loss_yesterday_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = now - timedelta(days=1)).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte =now - timedelta(days=1)).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte =now - timedelta(days=1)).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte =now - timedelta(days=1)).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })



class profit_loss_weekly_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = now - timedelta(days=7)).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte =now - timedelta(days=7)).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte =now - timedelta(days=7)).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte =now - timedelta(days=7)).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })



class profit_loss_monthly_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = now - timedelta(days=30)).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte =now - timedelta(days=30)).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte =now - timedelta(days=30)).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte =now - timedelta(days=30)).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })


class profit_loss_half_yearly_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = now - timedelta(days=(6 * 365 / 12))).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte =now - timedelta(days=(6 * 365 / 12))).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte =now - timedelta(days=(6 * 365 / 12))).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte =now - timedelta(days=(6 * 365 / 12))).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })



class profit_yearly_report(APIView):

    def get(self,request):

        order = Order.objects.filter(order_status="Completed", is_active=True,created_at__gte = now - timedelta(days=365)).values()
        purchase = Purchase.objects.filter(is_active=True,created_at__gte =now - timedelta(days=365)).values()
        expence = Expenses.objects.filter(is_active=True, created_at__gte =now - timedelta(days=365)).values()
        damage = DamageProducts.objects.filter(is_active=True, created_at__gte =now - timedelta(days=365)).values()

        order_total = order.aggregate(total=Sum('total'))
        order_count = order.count()

        purchase_total = purchase.aggregate(total=Sum('price'))
        purchase_count = purchase.count()
        purchase_due = purchase.aggregate(due=Sum('due_price'))

        expence_total = expence.aggregate(total=Sum('expence_amount'))
        expence_count = expence.count()

        damage_total = damage.aggregate(total=Sum('total_loss'))
        damage_count = damage.count()

        return Response({
            'order_total': order_total,
            'order_count': order_count,

            'expence': expence_total,
            'count': expence_count,

            'damage_total': damage_total,
            'damage_count': damage_count,

            'purchase_total': purchase_total,
            'purchase_count': purchase_count,
            'purchase_due':purchase_due,

        })