
# models import 
from inventory.bank_model.baccounts import BankAccounts

# serializer import 
from inventory.bank_serializer.bac_serializers import BankAccountsSerializers

# rest framework property import 
from rest_framework import generics

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

