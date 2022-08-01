from django.contrib import admin
from products.database.init_p import (
    Countreies,Sub_Categories,Brand,Categories,
)
from products.database.products import (
    Products,Product_images,ProductAttribute,
)
from products.database.slider import(
    Slider
)
from products.database.reviews import (
    ProductReview
)
from products.database.feature_product import (
    Banner,BannerProduct
)

admin.site.register(Categories)
admin.site.register(Sub_Categories)
admin.site.register(Brand)
admin.site.register(Countreies)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','review_star_count','review_comment_count','product_quantity']
admin.site.register(Products,ProductsAdmin)
# admin.site.register(Variation_with_Price_variant)
admin.site.register(ProductAttribute)
admin.site.register(Product_images)
admin.site.register(ProductReview)

admin.site.register(Banner)
class BannerProductAdmin(admin.ModelAdmin):
    list_display = [ 'id','banner','banner_product','is_active']
admin.site.register(BannerProduct,BannerProductAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','slidername','position','home_shown']
    
admin.site.register(Slider,SliderAdmin)
# admin.site.register(ColorVariation)
# admin.site.register(SizeVariation)
# admin.site.register(WeightVariation)
