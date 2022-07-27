
from django.shortcuts import render
from inventory.models import Purchase
from inventory.serializer import PurchaseSerialiers, PurchaseCreateSerializers
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status


# Create your views here.
'''
Purchase show 
Purchase Edit Delete and Update class
'''

# view List Function 

class PurchaseView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers


# Single View 

class PurchaseSingleView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers


#  Create View 

class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializers

    def post(self,request):
        data = request.data
        serializer = PurchaseCreateSerializers(data=data)

        if serializer.is_valid():
            obj = serializer.save()
            quan = serializer.validated_data['quantity']
            # pro_quan = obj.purchase_product.stock_count
            obj.purchase_product.stock_count += quan
            obj.purchase_product.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





# delete View 

class PurchaseDeleteView(generics.DestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiers


# Single Edit View 

class PurchaseEditView(generics.UpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializers