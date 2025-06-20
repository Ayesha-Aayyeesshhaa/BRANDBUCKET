from django.db import models
from .category import Category
from .product import Product


class Wishlist(models.Model):
    user = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)