'''
THis file contains the URL config 
_ flash sale 
_ flash product
'''


from django.urls import path
# importing Views 
from flash_sale.views import (

    # Flash Sale 
    FlashSale_createView,
    FlashSale_listView,
    FlashSale_singleView,
    FlashSale_update_deleteView,

    # Flash Sale Products
    FlashProducts_createView,
    FlashProduct_SingleView,
    FlashProduct_DeleteView
)

urlpatterns = []

flash_sale_URL = [
    path('create/',FlashSale_createView.as_view()),
    path('view/',FlashSale_listView.as_view()),
    path('view/<int:pk>/',FlashSale_singleView.as_view()),
    path('action/<int:pk>/',FlashSale_update_deleteView.as_view())
]

flash_products_URL = [
    path('product/create/',FlashProducts_createView.as_view()),
    path('product/view/<int:pk>/',FlashProduct_SingleView.as_view()),
    path('product/delete/<int:pk>/',FlashProduct_DeleteView.as_view())
    # path('')

]

urlpatterns += flash_products_URL
urlpatterns += flash_sale_URL

