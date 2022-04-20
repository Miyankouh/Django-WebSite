from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, DeleteView
from .models import Product


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     data = base_query.filter(is_active=True)
    #     return data


class ProductDetailView(DeleteView):
    template_name = 'product/product_detail.html'
    model = Product
    
    