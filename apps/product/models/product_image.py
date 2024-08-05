from django.db import models
from .main import Product


class ProductImage(models.Model):
    url = models.ImageField('extra_images')
    product = models.ForeignKey(Product, models.CASCADE)
