from django.urls import path

from apps.product.views import indexView

urlpatterns = [
    path('', indexView, name='home'),
    path('quick_view_modal_<int:pk>/', indexView, name='product_detail'),
]
