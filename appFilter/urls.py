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
    # DailySalesOrderTimeToTimeListView,
    DailyTotalSales,
)


from appFilter.views.products_filter import (
    HourlySales,
    Last24hoursSales,
    WeeklySalesView,
    MonthlySasleView,
    HalfYearlySalesView,
    YearlySalesView
)

from appFilter.views.expence_query import (
     
    HourlyExpenceView,
    last_24_hours_ExpenceView,
    WeeklyExpenceView,
    MonthlyExpenceView,
    HalfYearlyExpenceView,
    YearlyExpenceView,

    hourly_expence_view,

)

from appFilter.views.sale_reports import (
    SaleReports_View
)

from appFilter.views.views_sales import (
    passParams, 
    last_24_hour_list,
    hourly_View,
    daily_view,
    monthly_View,
    half_yearly_View,
    yearly_View
    
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
    # path('daily/sales/timetotime/list/', DailySalesOrderTimeToTimeListView.as_view()),
    path('total-sales-price-daily/',DailyTotalSales.as_view()),

    path('hour/',HourlySales.as_view()),
    path('last24/hours/sales/', Last24hoursSales.as_view()),
    path('weekly/sales/',WeeklySalesView.as_view()),
    path('monthly/sales/',MonthlySasleView.as_view()),
    path('half/yearly/sales/', HalfYearlySalesView.as_view()),
    path('yearly/sales/', YearlySalesView.as_view()),
]

sales_param_URL = [ 
    path('list/24/hours/', last_24_hour_list.as_view()),
    path('hourly/', hourly_View.as_view()),
    path('daily/', daily_view.as_view()),
    path('monthly/', monthly_View.as_view()),
    path('half/yearly/', half_yearly_View.as_view()),
    path('yearly/', yearly_View.as_view()),
]

expence_URL = [ 
    path('expence/last/hour/',HourlyExpenceView.as_view()),
    path('expence/last/24/hour/',last_24_hours_ExpenceView.as_view()),
    path('expence/weekly/',WeeklyExpenceView.as_view()),
    path('expence/monthly/',MonthlyExpenceView.as_view()),
    path('expence/half/yearly/',HalfYearlyExpenceView.as_view()),
    path('expence/yearly/',YearlyExpenceView.as_view()),
]
expence_date_total_URL = [ 
    path('expence/values/hour/',hourly_expence_view.as_view()),
]
sales_reports_URL = [
    path('sales/reports/',SaleReports_View.as_view()),
]


urlpatterns += sales_reports_URL
urlpatterns += sales_param_URL
urlpatterns += products_URL
urlpatterns += expence_URL
urlpatterns += expence_date_total_URL