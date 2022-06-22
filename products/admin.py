from django.contrib import admin
from products.database.init_p import (
    Countreies,Sub_Categories,Brand,Categories,
    ColorVariation,SizeVariation, WeightVariation
)
from products.database.products import (
    Products,Product_images,ProductAttribute,
    Variation_with_Price_variant
)
from products.database.slider import(
    Slider
)
from products.database.reviews import (
    ProductReview
)

admin.site.register(Categories)
admin.site.register(Sub_Categories)
admin.site.register(Brand)
admin.site.register(Countreies)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','review_star_count','review_comment_count']
admin.site.register(Products,ProductsAdmin)
admin.site.register(Variation_with_Price_variant)
admin.site.register(ProductAttribute)
admin.site.register(Product_images)
admin.site.register(ProductReview)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','slidername','position','home_shown']
    
admin.site.register(Slider,SliderAdmin)
admin.site.register(ColorVariation)
admin.site.register(SizeVariation)
admin.site.register(WeightVariation)
