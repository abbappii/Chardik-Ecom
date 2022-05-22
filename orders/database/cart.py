from accounts.models.initials import InitModels
from django.conf import settings
from django.db import models
from products.database.products import Products

'''
Cart
'''

# Cart Models 

class Cart(InitModels):
     user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='cart',
        on_delete=models.CASCADE
        )
    
     item = models.ForeignKey(Products,
      on_delete=models.CASCADE )

     quantity = models.IntegerField(default=1)

     purchased = models.BooleanField(default=False)

     def __str__(self):
         return f'{self.quantity} X {self.item}'


    # get item totol price individually from this function
    
     def get_total(self):
         total= self.item.new_price * self.quantity

         return total



    