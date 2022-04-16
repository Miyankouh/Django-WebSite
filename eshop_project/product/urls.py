from django.urls import path
from product import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<int:product_id>', views.product_detail, name='product-detail'),
]