from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    sort_by = request.GET.get('sort', 'name')
    products = Product.objects.all().order_by(sort_by)
    return render(request, 'home.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

