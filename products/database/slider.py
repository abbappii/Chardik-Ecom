
from django.db import models
from accounts.models.initials import InitModels

class Slider(InitModels):
    slidername = models.CharField(
        max_length=255,
        blank=True,
        null=True
        )
        
    slider_image = models.ImageField(upload_to = 'slider_images', blank = True)

    slug = models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=False)
    position = models.PositiveIntegerField()
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