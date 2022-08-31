
from django.db import models
from accounts.models.initials import InitModels

class Slider(InitModels):
    slidername = models.CharField(
        max_length=255,
        blank=True,
        null=True
        )
        
    slider_image = models.ImageField(upload_to = 'slider_images', blank = True)

    url_link = models.CharField(max_length=400,null=True,blank=True,verbose_name=
        "Slider URL Link")
    position = models.PositiveIntegerField(null=True)
    home_shown = models.BooleanField(default=True)

    category = models.ForeignKey(
        'products.Categories',
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Category',
        related_name='category_slider'
        )

    class Meta:
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.slidername