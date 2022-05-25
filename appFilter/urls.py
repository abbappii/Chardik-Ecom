from django.urls import path

# importing Views 
from appFilter.views.products_filter import (
    AllProductsView,ProductsUnderCategoryView
)




urlpatterns = []


products_URL = [
    path('products/',AllProductsView.as_view()),
    path('products/>category/',ProductsUnderCategoryView.as_view())
]

urlpatterns += products_URL