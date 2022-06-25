from django.db import models

# Create your models here.
class Pathao(models.Model):
    client_id= models.CharField(max_length=100)
    client_secret= models.CharField(max_length=1000)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    grant_type= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username


