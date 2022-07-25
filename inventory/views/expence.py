
from inventory.bank_model.baccounts import Expenses
from inventory.bank_serializer.expence_serializers import ExpenceSerializers, ExpenceListSerializers

from rest_framework import generics, status
from rest_framework.response import Response
from decimal import Decimal

'''
logic here
        - expence create
        - expence list
'''
class ExpenceCreateView(generics.GenericAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenceSerializers

    def post(self, request):
        data = request.data
        serializer = ExpenceSerializers(data=data)

        if serializer.is_valid():
            obj = serializer.save()

            ex = serializer.validated_data['expence_amount']
            # ex_amount = data['expence_amount']

            obj.account.amount -= Decimal(ex)
            obj.account.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# list view 
class ExpenceListView(generics.ListAPIView):
    queryset = Expenses.objects.filter(is_active=True)
    serializer_class = ExpenceListSerializers

# delete view 
class ExpenceDeleteView(generics.DestroyAPIView):
    queryset = Expenses.objects.filter(is_active=True)
    serializer_class = ExpenceSerializers