from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data
    
    

# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product/product_list.html', {
#         'products': products,
#     })


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product/product_detail.html', {
#         'product': product
#     })

class ProductDetailView(TemplateView):
    template_name = 'product/product_detail.html'

    def get_object_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        slug = kwargs['slug'] 
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context