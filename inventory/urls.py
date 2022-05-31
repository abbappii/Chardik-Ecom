
'''
This file contains the URL config of Inventory app
'''

from django.urls import path
from inventory.views.purchase_view import (
    PurchaseView,PurchaseSingleView,PurchaseCreateView,
    PurchaseEditView,PurchaseDeleteView

)

from inventory.views.supplier_view import (
    SupplierListView,SupplierEditApiView,SupplierCreateApiView,
    SupplierRetrieveView,SupplierDeleteApiView
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
    path('purchase/create/',PurchaseCreateView.as_view())
]

urlpatterns += supplier_URL
urlpatterns += purchase_URL