from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max

# Create your views here.

def product_list(request):
    console = ProductCategory(title='پلی استیشن', url_title='playstation')
    console.save()

    ps4 = Product(title='playstaion 4', price='15100', category=console, short_description='paly game', rating=4)
    ps4.save()


    products = Product.objects.all().order_by('title')
    number_of_prodoucts = products.count()
    avg_rating = products.aggregate(Avg("rating"))

    return render(request, 'product/product_list.html', {
        'products': products,
        'total_number_of_products': number_of_prodoucts,
        'avareg_ratings': avg_rating,
    })


def product_detail(request, slug):
    # try:
        # product = Product.objects.get(id=product_id)
    # except:
        # raise Http404()
    
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {
        'product': product
    })