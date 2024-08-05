from django.shortcuts import render

from apps.product.models import Product


def indexView(request):
    product = Product.objects.all()
    return render(request, 'index.html', {"product": product})
