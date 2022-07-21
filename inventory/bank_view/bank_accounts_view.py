
# models import 
from inventory.bank_model.baccounts import BankAccounts, DepositWithdraw

# serializer import 
from inventory.bank_serializer.bac_serializers import BankAccountsSerializers, DepositWithdrawSerializers

# rest framework property import 
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal


'''
    Bank accounts logic
        - create view
        - single view
        - list view
        - edit view
        - delete view
'''

# list view 
class BankAccountListView(generics.ListAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializers

# create view 
class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializers

# single view 
class BankAccountSingleView(generics.RetrieveAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializers

# edit view 
class BankAccountEditView(generics.UpdateAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializers

# delete view 
class BankAccountDeleteView(generics.DestroyAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializers


'''
    here logic for 
        deposit withdraw
            - list view
            - create view

'''

# list view 
class DepositWithdrawListView(generics.ListAPIView):
    queryset = DepositWithdraw.objects.all()
    serializer_class = DepositWithdrawSerializers


# create view 
class DepositWithdrawCreateView(generics.GenericAPIView):
    queryset = DepositWithdraw.objects.all()
    serializer_class = DepositWithdrawSerializers

    def post(self,request,format = None):
        data = request.data
        serializer = DepositWithdrawSerializers(data=data)

        if serializer.is_valid():
            obj = serializer.save()
            amount = data['amount']
            if obj.transfer_type == 'Deposit':
                obj.account.amount += Decimal(amount)
            else:
                obj.account.amount -= Decimal(amount)

            obj.account.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
