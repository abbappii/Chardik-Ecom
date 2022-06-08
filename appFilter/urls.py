from django.urls import path

# importing Views 
from appFilter.views.products_filter import (
    AllProductsView, ProductsUnderBrandView,ProductsUnderCategoryView, ProductsUnderCountryView,
    SingleCategoryProducts,SingleBrandProducts,SingleCoutryProducts
)


urlpatterns = []


products_URL = [
    path('products/',AllProductsView.as_view()),
    path('products/category/',ProductsUnderCategoryView.as_view()),
    path('products/category/<int:pk>/',SingleCategoryProducts.as_view()),
    path('products/brand/', ProductsUnderBrandView.as_view(), name='products-under-brand'),
    path('products/brand/<int:pk>/',SingleBrandProducts.as_view()),
    path('products/country/', ProductsUnderCountryView.as_view(), name='products-under-country'),
    path('products/country/<int:pk>/',SingleCoutryProducts.as_view()),


]

urlpatterns += products_URL