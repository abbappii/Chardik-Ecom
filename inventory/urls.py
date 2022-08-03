
'''
This file contains the URL config of Inventory app
'''

from django.urls import path
from inventory.views.purchase_view import (
    PurchaseView,PurchaseSingleView,PurchaseCreateView,
    PurchaseEditView,PurchaseDeleteView,
    SupplierDue_ReportsView

)

from inventory.views.supplier_view import (
    SupplierListView,SupplierEditApiView,SupplierCreateApiView,
    SupplierRetrieveView,SupplierDeleteApiView
)

from inventory.views.bank_accounts_view import (
    BankAccountCreateView,
    BankAccountDeleteView,
    BankAccountEditView,
    BankAccountListView,

    AllBankAccountTotalMoneyView,

    BankAccountSingleView,
    DepositWithdrawListView,
    DepositWithdrawCreateView,
    DepositWithdrawDeleteView
)

from inventory.views.name_outlet import (
    NameListView,
    NameCreateView,
    NameDeleteView,
    OutletListView,
    OutletCreateView,
    OutletDeleteView, 
)

from inventory.views.expence import (
    
    ExpenceCreateView, 
    ExpenceListView, 
    ExpenceDeleteView

    )

urlpatterns = []

supplier_URL = [
    path('supplier/',SupplierListView.as_view()),
    path('supplier/view/<int:pk>/',SupplierRetrieveView.as_view()),
    path('supplier/update/<int:pk>/',SupplierEditApiView.as_view()),
    path('supplier/delete/<int:pk>/',SupplierDeleteApiView.as_view()),
    path('supplier/create/',SupplierCreateApiView.as_view())
]

purchase_URL = [
    path('purchase/',PurchaseView.as_view()),
    path('purchase/view/<int:pk>/',PurchaseSingleView.as_view()),
    path('purchase/update/<int:pk>/',PurchaseEditView.as_view()),
    path('purchase/delete/<int:pk>/',PurchaseDeleteView.as_view()),
    path('purchase/create/',PurchaseCreateView.as_view()),
    path('supplier/due/reports/',SupplierDue_ReportsView.as_view())
]


bank_accounts_URL = [ 
    path('baccounts/list/view/', BankAccountListView.as_view()),
    path('baccounts/single/view/<int:pk>/', BankAccountSingleView.as_view()),
    path('baccounts/create/view/', BankAccountCreateView.as_view()),
    path('baccounts/edit/view/<int:pk>/', BankAccountEditView.as_view()),
    path('baccounts/delete/view/<int:pk>/', BankAccountDeleteView.as_view()),

    path('baccounts/total/amount/view/', AllBankAccountTotalMoneyView.as_view()),

    path('baccounts/depositwithraw/list/view/', DepositWithdrawListView.as_view()),
    path('baccounts/depositwithraw/create/view/', DepositWithdrawCreateView.as_view()),
    path('baccounts/depositwithraw/delete/view/<int:pk>/',DepositWithdrawDeleteView.as_view()),

]

name_outlet_URL = [ 

    path('expence/name/list/view/',NameListView.as_view()),
    path('expence/name/create/',NameCreateView.as_view()),
    path('expence/name/delete/<int:pk>/', NameDeleteView.as_view()),

    path('expence/outlet/list/view/',OutletListView.as_view()),
    path('expence/outlet/create/',OutletCreateView.as_view()),
    path('expence/outlet/delete/<int:pk>/', OutletDeleteView.as_view()),
]

expence_URL = [ 
    path('expence/create/',ExpenceCreateView.as_view()),
    path('expence/list/view/',ExpenceListView.as_view()),
    path('expence/delete/<int:pk>/', ExpenceDeleteView.as_view()),
]

urlpatterns += supplier_URL
urlpatterns += purchase_URL
urlpatterns += bank_accounts_URL
urlpatterns += name_outlet_URL
urlpatterns += expence_URL