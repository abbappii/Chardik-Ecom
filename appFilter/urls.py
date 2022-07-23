from django.urls import path

# importing Views 
from appFilter.views.products_filter import (
    AllProductsView,
    ProductsUnderBrandView,
    ProductsUnderCategoryView, 
    ProductsUnderCountryView,
    SingleCategoryProducts,
    SingleBrandProducts,
    SingleCoutryProducts,
    Prouduct_by_review_count,
    PopularProductList,
    LatestProductList,
    TopSalesProductsListView, 
    DailySalesOrderTimeToTimeListView,
    # DailyTotalSalesRevenue,
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

    path('product-by-review-count/',Prouduct_by_review_count.as_view()),
    path('popular-products/', PopularProductList.as_view()),
    path('latest-products/', LatestProductList.as_view()),
    path('top-sales-product/', TopSalesProductsListView.as_view()),

    # path('low-to-high-price/', PriceLowToHighListView.as_view()),
    # path('high-to-low-price/', PriceHighToLowListView.as_view()),
    path('daily-sales/', DailySalesOrderTimeToTimeListView.as_view()),
    # path('total-sales-price-daily/',DailyTotalSalesRevenue.as_view()),
]

urlpatterns += products_URL