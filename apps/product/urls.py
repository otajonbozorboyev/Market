from django.urls import path

from apps.product.views import indexView

urlpatterns = [
    path('', indexView, name='home'),
]