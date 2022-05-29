from django.db import models
from accounts.models.initials import InitModels
'''
Category
sub Category
brand 

country 
size 
color
weight 
'''

# Product  categories 
class Categories(InitModels):
    category_name=models.CharField(
        max_length=100,
        null=True, 
        blank=True
        )
    slug=models.SlugField(
        max_length=255, 
        null=True, 
        blank=True,
        unique=True
        )
    image=models.ImageField(
        upload_to='categories', 
        blank=True)
    category_code=models.CharField(
        max_length=100, 
        null=True, 
        blank=True
        )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Category"



#Product Sub Categories
class Sub_Categories(InitModels):
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE, 
        related_name='categories'
        )
    sub_category_name=models.CharField(
        max_length=100, 
        null=True, 
        blank=True
        )
    slug=models.SlugField(
        max_length=255, 
        null=True, 
        blank=True,
        unique=True
        )
    image=models.ImageField(
        upload_to='sub_categories', 
        blank=True
        )
    description=models.TextField(
        max_length=1500, 
        null=True, 
        blank=True
        )

    def __str__(self) -> str:
        return self.sub_category_name

    class Meta:
        verbose_name_plural = 'Sub Category'



#Products Brands
class Brand(InitModels):
    name = models.CharField(max_length=255,unique=True)
    brand_website = models.CharField(max_length=255,unique=True,null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Brand"

#Products Countries
class Countreies(InitModels):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"
