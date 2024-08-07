from django.shortcuts import render, redirect

from apps.product.models import Product


def indexView(request, pk=None):
    product = Product.objects.all()
    if pk:
        product_detail = Product.objects.prefetch_related().filter(pk=pk).first()
        print(type(product_detail))
        return render(request, 'product-details.html', {"product_detail": product_detail})
    return render(request, 'index.html', {"product": product})
