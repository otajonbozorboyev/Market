from django.db import models
from apps.user.models import Category


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images')
    description_title = models.CharField(max_length=200)
    description_base = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    percent_price = models.IntegerField(null=True, blank=True)
    ctg = models.ManyToManyField(Category)
    count_view = models.IntegerField(default=0)
    # Count(BASCET COUNT - SERIALIZER)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.discount_price:
            self.discount_price = self.price
        self.percent_price = int(((int(self.price) - int(self.discount_price)) / int(self.price)) * 100)
        return super().save(*args, **kwargs)
