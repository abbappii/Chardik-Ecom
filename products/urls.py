
from django.urls import path
from products.views.prodcuts_logic import (
    ProductListViewSet,
    # ProductListViewAdmin,
    ProductCreateView,
    ProductRetUpDesViewSet,

    # ProductVariationCreate,
    # ProductVariationSingle_updateView,
    # ProductVariation_DeleteView,
    # ProductVariationSingleView,
    ProductSingleView,

    # ProductVariationList,
)

from products.views.products_init_logic import (
    CategoriesViewSet, 
    CategoriesUpdateDelete, 

    SubCategoriesListView, 
    SubCategoryCreateView,
    SubCategorySingleView,
    SubCategoryUpdateView,
    SubCategoryDeleteView,

    BrandView,
    BrandUpdateDelete,
    
    CountryView,
    CountryUpdateDelete,

    # ColorVariationListAPIview,
    # ColorVariationSingleAPIview,
    # SizeVariationListAPIview,
    # SizeVariationSingleAPIview,
    # WeightVariationListAPIview,
    # WeightVariationSingleAPIview
     
)

from products.views.product_review_logic import (
    ProducReviewtListView, 
    ProductReviewCreateView,
    ProductReviewRetrieveView, 
    ProductReviewEditView,
    ProductReviewDeleteView
)


from products.views.slider_logic import (
    SliderListView, 
    SliderSingleView,
    SliderCreateView,
    SliderEditView,
    SliderDeleteView
)


from products.views.feature_products_logic import (
    FeatureProductListView,
    FeatureProductCreateView,
    FeatureProductUpdateView,
    FeatureProductDeleteView,
)

urlpatterns = []


urlpatterns_category = [
    path('categories/', CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesUpdateDelete.as_view(), 
        name='categories_update_delete'),

    path('sub_categories/list/', SubCategoriesListView.as_view(), name='sub_categories_list'),
    path('subcategory/create/', SubCategoryCreateView.as_view(), name='sub_category_create'),
    path('sub_categories/single/<int:pk>/', SubCategorySingleView.as_view(),
        name='sub_categories_update_delete'),
    path('sub_category/update/<int:pk>/',SubCategoryUpdateView.as_view()),
    path('sub_category/delete/<int:pk>/',SubCategoryDeleteView.as_view()),
]

urlpatterns_product = [ 
    
    path('product/', ProductListViewSet.as_view(), name='products' ),

    # path('product/list/admin/view/', ProductListViewAdmin.as_view()),

    path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    path('product/update-delete/<int:pk>/',ProductRetUpDesViewSet.as_view(), 
        name='products_delete_update' ),
    path('product/single/<int:pk>/',ProductSingleView.as_view()),
    
    # products renderer url 
    # path('product/', ProductListViewSet.as_view(), name='products' ),
    # path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    # path('product/<slug:slug>/',ProductDetail.as_view(), name='products_detail' ),

    # product Variation URL
    # path('product/variation/create/',ProductVariationCreate.as_view()),
    # path('product/variation/view/<int:pk>/',ProductVariationSingleView.as_view()),
    # path('product/variation/update/<int:pk>/',ProductVariationSingle_updateView.as_view()),
    # path('product/variation/delete/<int:pk>/',ProductVariation_DeleteView.as_view()),
    # path('product/variation/list/',ProductVariationList.as_view()),

]


urlpatterns_brand_countries = [ 
    path('brand/', BrandView.as_view(), name='brand' ),
    path('brand/<int:pk>/', BrandUpdateDelete.as_view(), name='brand_update_delete' ),
    path('countries/', CountryView.as_view(), name='country' ),
    path('countries/<int:pk>/', CountryUpdateDelete.as_view(), name='country_update_delete' ),
]


urlpatterns_productsReview = [ 
    path('review/',ProducReviewtListView.as_view()),
    path('review/create/',ProductReviewCreateView.as_view()),
    path('review/view/<int:pk>/', ProductReviewRetrieveView.as_view()),
    path('review/update/<int:pk>/',ProductReviewEditView.as_view()),
    path('review/delete/<int:pk>/',ProductReviewDeleteView.as_view()),
]

urlpatterns_slider = [ 
    path('slider/',SliderListView.as_view()),
    path('slider/create/',SliderCreateView.as_view()),
    path('slider/view/<int:pk>/', SliderSingleView.as_view()),
    path('slider/update/<int:pk>/',SliderEditView.as_view()),
    path('slider/delete/<int:pk>/',SliderDeleteView.as_view()),
]

urlpatterns_feature_products = [ 
    path('feature/products/list/',FeatureProductListView.as_view()),
    path('feature/product/create/',FeatureProductCreateView.as_view()),
    path('feature/product/update/view/<int:pk>/',FeatureProductUpdateView.as_view()),
    path('feature/product/delete/',FeatureProductDeleteView.as_view()),
]
# urlpatterns_attribute = [
#     path('color/',ColorVariationListAPIview.as_view()),
#     path('color/<int:pk>/',ColorVariationSingleAPIview.as_view()),
    
#     path('size/',SizeVariationListAPIview.as_view()),
#     path('size/<int:pk>/',SizeVariationSingleAPIview.as_view()),

#     path('weight/',WeightVariationListAPIview.as_view()),
#     path('weight/<int:pk>/',WeightVariationSingleAPIview.as_view())
# ]


# urlpatterns += urlpatterns_attribute
urlpatterns += urlpatterns_category
urlpatterns += urlpatterns_product
urlpatterns += urlpatterns_brand_countries
urlpatterns += urlpatterns_productsReview
urlpatterns += urlpatterns_slider
urlpatterns += urlpatterns_feature_products