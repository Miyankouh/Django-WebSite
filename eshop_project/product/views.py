from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {
        'products': products
    })


def product_detail(request, product_id):
    # try:
        # product = Product.objects.get(id=product_id)
    # except:
        # raise Http404()
    
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_detail.html', {
        'product': product
    })