
from django.db import models
from accounts.models.initials import InitModels


class AddDamageProduct(InitModels):
    product = models.ForeignKey('products.Products',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Damage Product",
        related_name="damage_product"
    )
    quantity = models.IntegerField(
        null=True,
        verbose_name="quantity"
        )
    loss_per_unit = models.PositiveIntegerField(default=0)


    def __unicode__(self):
        return str(self.product.product_name)

    class Meta:
        verbose_name_plural = 'Add Damage Product'


class DamageProducts(InitModels):
    ref = models.CharField(max_length=200,null=True, blank=True)
    outlet = models.ForeignKey(
        'inventory.Outlet', 
        on_delete=models.SET_NULL, 
        null=True
        )
    date = models.CharField(max_length=255,null=True, blank=True)
    responsible_person = models.ForeignKey(
        'accounts.Profile', 
        on_delete=models.SET_NULL, 
        null=True
        )

    products_ids = models.ManyToManyField(
        AddDamageProduct,
        related_name='damage_product_list'
        )

    total_loss = models.PositiveIntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ref

    class Meta:
        verbose_name_plural = 'Damage Products List'

