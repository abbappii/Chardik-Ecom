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
    # DailyTotalSales,
)


# from appFilter.views.products_filter import (
#     HourlySales,
#     Last24hoursSales,
#     WeeklySalesView,
#     MonthlySasleView,
#     HalfYearlySalesView,
#     YearlySalesView
# )

from appFilter.views.expence_query import (
     
    HourlyExpenceView,
    last_24_hours_ExpenceView,
    
    daily_ExpenceView,

    WeeklyExpenceView,
    MonthlyExpenceView,
    HalfYearlyExpenceView,
    YearlyExpenceView,

    hourly_expence_view,
    twenty_4_hours_expence_view,
    daily_expence_view,
    monthly_expence_view,
    half_yearly_expence_view,
    yearly_expence_view,

)

from appFilter.views.sale_reports import (
    SaleReports_View
)

from appFilter.views.views_sales import (
    # passParams, 
    last_24_hour_list,
    hourly_View,
    daily_view,
    monthly_View,
    half_yearly_View,
    yearly_View,
    sales_all
    
    )

from appFilter.views.dashboard import (
    Purchase_ofSupplier_View,
    Sale_of_CustomersView
)

from appFilter.views.profit_loss import (
    
    profit_loss_daily_report,
    profit_loss_yesterday_report,
    
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
    # path('total-sales-price-daily/',DailyTotalSales.as_view()),

    # path('hour/',HourlySales.as_view()),
    # path('last24/hours/sales/', Last24hoursSales.as_view()),
    # path('weekly/sales/',WeeklySalesView.as_view()),
    # path('monthly/sales/',MonthlySasleView.as_view()),
    # path('half/yearly/sales/', HalfYearlySalesView.as_view()),
    # path('yearly/sales/', YearlySalesView.as_view()),
]

sales_param_URL = [ 
    path('sales/list/last-24-hours/', last_24_hour_list.as_view()),
    path('sales/list/hourly/', hourly_View.as_view()),
    path('sales/list/daily/', daily_view.as_view()),
    path('sales/list/monthly/', monthly_View.as_view()),
    path('sales/list/half-yearly/', half_yearly_View.as_view()),
    path('sales/list/yearly/', yearly_View.as_view()),
]

sales_reports_URL = [
    path('sales/totals/',SaleReports_View.as_view()),
    path('sales-all/',sales_all.as_view()),
]

expence_URL = [ 
    path('expense/totals/last-hour/',HourlyExpenceView.as_view()),
    path('expense/totals/last-24-hour/',last_24_hours_ExpenceView.as_view()),

    path('expense/totals/daily/',daily_ExpenceView.as_view()),

    path('expense/totals/weekly/',WeeklyExpenceView.as_view()),
    path('expense/totals/monthly/',MonthlyExpenceView.as_view()),
    path('expense/totals/half-yearly/',HalfYearlyExpenceView.as_view()),
    path('expense/totals/yearly/',YearlyExpenceView.as_view()),
]
expence_date_total_URL = [ 
    
    path('expense/list/hour/',hourly_expence_view.as_view()),
    path('expense/list/24-hours/',twenty_4_hours_expence_view.as_view()),
    path('expense/list/daily/',daily_expence_view.as_view()),
    path('expense/list/monthly/',monthly_expence_view.as_view()),
    path('expense/list/half-yearly/',half_yearly_expence_view.as_view()),
    path('expense/list/yearly/',yearly_expence_view.as_view()),

]

dashboard_URL = [
    path('purchase/supplier/',Purchase_ofSupplier_View.as_view()),
    path('saling/customer/',Sale_of_CustomersView.as_view())
]

urlpatterns_profit_loss = [ 
    path('profit-loss/daily/', profit_loss_daily_report.as_view()),
    path('profit-loss/yesterday/', profit_loss_yesterday_report.as_view()),
    
]

urlpatterns += sales_reports_URL
urlpatterns += sales_param_URL
urlpatterns += products_URL
urlpatterns += expence_URL
urlpatterns += expence_date_total_URL
urlpatterns += dashboard_URL
urlpatterns += urlpatterns_profit_loss 