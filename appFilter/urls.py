from django.urls import path

# importing Views 
from appFilter.views.products_filter import (
    AllProductsView, ProductsUnderBrandView,ProductsUnderCategoryView
)


urlpatterns = []


products_URL = [
    path('products/',AllProductsView.as_view()),
    path('products/>category/',ProductsUnderCategoryView.as_view()),
    path('products/brand/', ProductsUnderBrandView.as_view(), name='products-under-brand'),
]

urlpatterns += products_URL