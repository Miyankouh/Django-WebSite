from django.urls import path
from product import views

urlpatterns = [
    path('', views.product_list),
    path('<int:product_id>', views.product_detail),
]