from django.contrib import admin
from . models import Product
from ..user.models import Category

admin.site.register(Product)
admin.site.register(Category)