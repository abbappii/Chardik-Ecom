from django.contrib import admin
from products.database.init import (
    Countreies,Sub_Categories,Brand,Categories
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

admin.site.register(Categories)
admin.site.register(Sub_Categories)
admin.site.register(Brand)
admin.site.register(Countreies)
admin.site.register(Products)
admin.site.register(ProductAttribute)
admin.site.register(Product_images)
admin.site.register(ProductReview)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','slidername','position','home_shown']
    
admin.site.register(Slider,SliderAdmin)