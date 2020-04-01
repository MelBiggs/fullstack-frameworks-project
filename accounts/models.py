from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(User, related_name="favourites",
                             on_delete=models.CASCADE,
                             related_query_name="favourite", null=True)
    product = models.ForeignKey(Product, null=True)
