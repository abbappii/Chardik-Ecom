
from django.db import models

from django.utils.translation import gettext_lazy as _

from accounts.models.initials import InitModels
from django.db.models import Sum,Count



'''
Products 
attribute 
'''

#Product Attribute model
class ProductAttribute(InitModels):
    name = models.CharField(max_length=255,unique=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # custom Property 
    def all_products(self):
        return [products for products in self.Category_products.all()]

    class Meta:
        verbose_name_plural = "Product Attribute"

  
#Product Model
class Products(InitModels):
    brand = models.ForeignKey(
        'products.Brand', 
        on_delete=models.CASCADE,
        related_name= 'brand'
        )
    country = models.ForeignKey(
        'products.Countreies',
        on_delete=models.CASCADE, related_name='country'
        )
    
    category = models.ManyToManyField('products.Categories',
        related_name='Category_products')
    sub_category = models.ManyToManyField('products.Sub_Categories',
        related_name='Sub_category_products')

    product_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
        )
    slug = models.SlugField(
        max_length=250, 
        null=False, blank=False, unique=True)
    meta = models.TextField(
        max_length=500, 
        null=True, 
        blank=True
        )
    short_descriptions = models.CharField(
        max_length=1200, 
        null=True, 
        blank=True,
        verbose_name='Short DesColorVariationcription'
        )
    long_description = models.TextField(
        null=True, 
        blank=True,
        verbose_name='Long Description'
        )
    alter_text = models.CharField(
        max_length=400, 
        null=True, 
        blank=True
        )
    tags = models.TextField(null=True,blank=True)
    
    sku = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='SKU',
        null=True
        )
    # upc = models.CharField(
    #     max_length=12,
    #     unique=True,
    #     verbose_name='UPC'
    #     )
    feature_image=models.ImageField(upload_to='products',null=True)
    # regular_price = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    #     default=0.00
    #     )
    # new_price = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    #     default=0.00
    #     )
    attribute = models.CharField(max_length=1000, null=True, blank=True)
    
    regular_price = models.FloatField(null=True,blank=True)
    selling_price = models.FloatField(null=True,blank=True)
    reseller_price = models.FloatField(null=True, blank=True)
    
    sold_count = models.IntegerField(null=True,blank=True)
    expire_date = models.DateField(auto_now_add=False,null=True,blank=True)
    is_stock = models.BooleanField(default=True,verbose_name="Is Stock")


    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name_plural = "Product"


    # Custom Property 

    @property
    def get_category(self):
        category = [category.category_name for category in self.category.all()]
        return category
    

    @property
    def get_sub_category(self):
        sub_category = [ sub_category.sub_category_name for  sub_category in \
             self.sub_category.all()]
        return sub_category


    @property
    def review_star_count(self):
        # review count by star
        sum_count = self.reviews.aggregate(Sum('star_count'))['star_count__sum']
        total_count = self.reviews.aggregate(Count('star_count'))['star_count__count']
        if sum_count is None:
            return sum_count == 0 
        else: 
            avg_count = round((sum_count/total_count),2)
            return avg_count


    @property
    def review_comment_count(self):
        # review count by comment
        comment_count = self.reviews.count()
        return comment_count


    @property
    def is_top_sale(self):
        # check sold_count quantity
        if self.sold_count > 20:
            return True
        else:
            return False

    # Quantity property 
    @property
    def product_quantity(self):
        if self.purchase_product:
            # return self.purchase.quantity
            # print()
            return self.purchase_product.\
                    aggregate(Sum('quantity'))['quantity__sum']
        else:
            return f"0.00"
        # return self.purchase_product.quantity if self.purchase_product else "none"

## Product Variation with Price and variant 

# class Variation_with_Price_variant(InitModels):

#     product = models.ForeignKey('products.Products',on_delete=models.CASCADE,
#         null=True,verbose_name="Product",related_name="variant")
#     # variation 
#     size = models.ForeignKey('products.SizeVariation',on_delete=models.SET_NULL,
#         null=True,blank=True,verbose_name="Product Size")
#     color = models.ForeignKey('products.ColorVariation',on_delete=models.SET_NULL,
#         null=True,blank=True,verbose_name="Product Color")
#     weight = models.ForeignKey('products.WeightVariation',on_delete=models.CASCADE,
#         null=True,blank=True,verbose_name="Product Weight")
    
#     # price 
#     regular_price = models.FloatField(null=True,blank=True)
#     selling_price = models.FloatField(null=True,blank=True)


#     def __str__(self):
#         return str(self.product)

#     class Meta:
#         verbose_name_plural = "Product Variation"



# product images 
class Product_images(InitModels):
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE, 
        related_name='product_image')
    image=models.ImageField(upload_to='product_image_gallery', blank=True)
    

    class Meta:
        verbose_name_plural = "Product Image"


    